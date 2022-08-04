# It is desired that you model and implement, in the language of your choice, an interpreter for a subset of the Prolog language:
# (a) You must know how to handle facts, rules, and queries. These will all consist of expressions, which can take one of the following forms:

# i. Atom: Any alphanumeric string beginning with a lowercase character. For example:

# hello
# ci3641
# quickSort

# ii. Variable: Any alphanumeric string that begins with an uppercase character. For example:

# Hello
# CI3641
# QuickSort

# iii. Structure: An atom, followed by a sequence, parentized and separated by commas, of other expressions. For example:
# f(x, y)
# quickSort(input, Output)
# in(c(c(e,P), t(i, o(N))))

# (b) Once the program has started, it will repeatedly prompt the user for an action to proceed. Such an action can be:

# i. DEF <expression> [<expression>].
# Defines a new fact or rule, represented by the first <expression> (in the previously set
# previously established format).
# If the list of expressions (after the first one) is empty, the definition corresponds to a fact.
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Set, Union

class Prolog():
    def __init__(self) -> None:
        self.digraph = nx.DiGraph()
        self.node = 0
        self.labels = {}
        self.ilabels = {}

    def begin_program(self):
        print("Welcome to a subset of Prolog")

        while True:
            action = input("Enter an action: ")
            param = action.split(" ", 1)
            act = param.pop(0).lower()
            if act == "def" or act == "1":
                if len(param) == 1:
                    self.define_fact(param[0])
                elif len(param) > 1:
                    self.define_rule(param)
                else:
                    print("Error: invalid number of parameters")
            elif act == "ask" or act == "2":
                if len(param) == 1:
                    self.ask(param[0])
                else:
                    print("Error: invalid number of parameters")
            elif act == "exit" or act == "3":
                break
            else:
                print("Error: invalid action")

    def define_fact(self, fact: str):
        if fact[0].isupper():
            print(f"Error: invalid fact, {fact} is not an atom")
        if "(" in fact:
            est = self.extract_struct(fact)
            if any(x[0].isupper() for x in est):
                print(f"Error: invalid fact, {fact} contains a variable")
                return
            if est[1] == "":
                print(f"Error: invalid fact, {fact} is not a structure")
                return
            if not self.digraph.has_node(self.ilabels[est[0]]):
                self.digraph.add_node(self.node)
                self.labels[self.node] = est[0]
                self.ilabels[est[0]] = self.node
                self.node += 1

            self.digraph.add_edge(self.ilabels[est[0]], self.node)
            self.labels[self.node] = est[1]
            self.ilabels[est[1]] = self.node
            self.node += 1
            for i in range(2, len(est)):
                self.digraph.add_edge(self.node-1, self.node)
                self.labels[self.node] = est[i]
                self.ilabels[est[i]] = self.node
                self.node += 1
        else:
            if self.digraph.has_node(self.ilabels[fact]):
                print(f"Error: fact {fact} already defined")
                return
            self.digraph.add_node(self.node)
            self.labels[self.node] = fact
            self.ilabels[fact] = self.node
            self.node += 1
        print(f"It was defined the fact {fact}")

    @staticmethod
    def extract_struct(fact: str) -> List[str]:
        """
        Extracts the structure of a fact or rule
        Given atom(a, b, c), returns [atom, a, b, c]
        """
        est = []
        est.append(fact[:fact.find("(")])
        est.extend(fact[fact.find("(")+1:fact.find(")")].split(","))
        return [x.lstrip() for x in est]

    def define_rule(self, rule: list):
        if rule[0][0].isupper():
            print(f"Error: invalid rule, {rule[0]} is not an atom")
        else:
            consequent = rule[0]
            antecedents = rule[1:]
            for antecedent in antecedents:
                if antecedent[0].isupper():
                    print(f"Error: invalid rule, {antecedent} is not an atom")
                else:
                    self.digraph.add_edge(antecedent, consequent)
            print(f"It was defined the rule {rule}")

    def ask(self, query: str):
        if query[0].isupper():
            print(f"Error: invalid query, {query} is not an atom")
        else:
            if self.digraph.has_node(query):
                print(f"{query} is a fact")
            else:
                print(f"{query} is not a fact")
                print("The query has failed")

    def draw_graph(self):
        nx.draw(self.digraph, labels=self.labels , with_labels=True)
        plt.show()




