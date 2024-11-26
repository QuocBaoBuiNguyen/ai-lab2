import itertools

class Resolution:

    def pl_resolution(self, KB, alpha_statement):
        clauses = []
        new = []
        kb_clauses_arr = []
        
        for clause in KB:
            kb_clauses_arr.append(self.parse_cnf_clause(clause))
        
        for kb_clause in kb_clauses_arr:
            self.add_new_clause_to_kb(clauses, kb_clause)

        alpha_negate_arr = self.negate_clause(alpha_statement)
        for alpha_negate_clause in alpha_negate_arr:
            self.add_new_clause_to_kb(clauses, alpha_negate_clause)
        
        result = []
        while True:
            pairs = itertools.combinations(range(len(clauses)), 2)
            
            resolvents = []
            for pair in pairs:
                resolvent = self.resolve(clauses[pair[0]], clauses[pair[1]], clauses)
                if resolvent and resolvent not in resolvents:
                    resolvents.append(resolvent)
            
            resolvents = list(itertools.chain.from_iterable(resolvents))
            result.append(resolvents)

            if not resolvents:
                return result, False
            else:
                if ['{}'] in resolvents:
                    return result, True
                else:
                    for res in resolvents:
                        clauses.append(res)            

    def resolve(self, clause_i, clause_j, clauses):
        resolvent = []
        
        for atom in clause_i:
            negate_atom = self.negate_atom(atom)
            if negate_atom in clause_j:
                new_ci = clause_i.copy()
                new_cj = clause_j.copy()
                new_ci.remove(atom)
                new_cj.remove(negate_atom)
                if not new_ci and not new_cj:
                    resolvent.append(['{}'])
                else:
                    clause = new_ci + new_cj
                    clause = self.remove_duplicates_and_sort(clause)
                    if not self.check_complementary(clause) and clause not in clauses:
                        resolvent.append(clause)
        return resolvent
    
    def remove_duplicates_and_sort(self, clause):
            clause = list(dict.fromkeys(clause))

            tuple_form = []
            for atom in clause:
                if atom[0] == '-':
                    tuple_form.append((atom[1], -1))
                else:
                    tuple_form.append((atom[0], 1))
            tuple_form.sort()

            res = []
            for tup in tuple_form:
                if tup[1] == -1:
                    res.append('-' + tup[0])
                else:
                    res.append(tup[0])
            return res

    def add_new_clause_to_kb(self, kb, clause):
        if kb is not None and clause not in kb and not self.check_complementary(clause):
            kb.append(clause)

    def check_complementary(self, clause):
        for atom in clause:
            if self.negate_atom(atom) in clause:
                return True
        return False

    def parse_cnf_clause(self, clause):
        # return list(filter(lambda x: x != 'OR', clause))
        return clause.replace(" ", "").split("OR")
        # return clause.split("OR")
    
    def negate_clause(self, clause):
        atom_arr = self.parse_cnf_clause(clause)
        res = []
        for atom in atom_arr:
            res.append([self.negate_atom(atom)])            
        return res

    def negate_atom(self, atom):
        if atom[0] == '-':
            return atom[1:]
        else:
            return '-' + atom[0]
