"""Main class definition for the Intervals conjunctive domain.

TODO(masotoud): fix the docstrings re: intervals, signs.
"""
import z3
from .abstract import ReducedProductAbstractState
from algorithms import bilateral
from domains.z3_variables import Z3VariablesDomain

class ReducedProductDomain(Z3VariablesDomain):
    """Represents an abstract space over the sign of variables.
    """
    def __init__(self, variables, domain_A, domain_B):
        """Constructs a new IntervalDomain, with variables named in variables.

        variables should be a list of variable names
        """
        Z3VariablesDomain.__init__(self, variables, z3.Int)
        self.domain_A = domain_A
        self.domain_B = domain_B

    def gamma_hat(self, alpha):
        """Returns a formula describing the same states as alpha.
        """
        return z3.And(self.domain_A.gamma_hat(alpha.state_A),
                      self.domain_B.gamma_hat(alpha.state_B))

    def join(self, elements):
        """Returns the join of a set of abstract states.

        join([ alpha_1, alpha_2, ..., alpha_n ]) is the smallest alpha
        containing all alpha_1, ..., alpha_n. It may not be in elements.
        """
        elements_A = [element.state_A for element in elements]
        elements_B = [element.state_B for element in elements]
        joined_A = self.domain_A.join(elements_A)
        joined_B = self.domain_B.join(elements_B)
        joined = ReducedProductAbstractState(joined_A, joined_B)
        return self.reduce(joined)

    def meet(self, elements):
        """Returns the meet of a set of abstract states.

        join([ alpha_1, alpha_2, ..., alpha_n ]) is the greatest alpha
        contained by all alpha_1, ..., alpha_n. It may not be in elements.
        """
        elements_A = [element.state_A for element in elements]
        elements_B = [element.state_B for element in elements]
        met_A = self.domain_A.meet(elements_A)
        met_B = self.domain_B.meet(elements_B)
        met = ReducedProductAbstractState(met_A, met_B)
        # TODO: should we reduce?
        return met

    def abstract_consequence(self, lower, upper):
        """Returns the "abstract consequence" of lower and upper.

        The abstract consequence must be a superset of lower and *NOT* a
        superset of upper.

        TODO: does this work?
        """
        consequence_A = self.domain_A.abstract_consequence(
            lower.state_A, upper.state_A)
        consequence_B = self.domain_B.abstract_consequence(
            lower.state_B, upper.state_B)
        return ReducedProductAbstractState(consequence_A, consequence_B)

    # Converts one concrete set of variables into an abstract element
    def beta(self, sigma):
        """Returns the least abstract state describing sigma.

        Sigma should be an Z3VariablesState. See Definition 3.4 in:
        Thakur, A. V. (2014, August). Symbolic Abstraction: Algorithms and
        Applications (Ph.D. dissertation). Computer Sciences Department,
        University of Wisconsin, Madison.
        """
        beta_A = self.domain_A.beta(sigma)
        beta_B = self.domain_B.beta(sigma)
        return ReducedProductAbstractState(beta_A, beta_B)

    @property
    def top(self):
        """Returns the least upper bound of the entire abstract space.
        """
        top_A = self.domain_A.top
        top_B = self.domain_B.top
        return ReducedProductAbstractState(top_A, top_B)

    @property
    def bottom(self):
        """Returns the greatest lower bound of the entire abstract space.
        """
        bottom_A = self.domain_A.bottom
        bottom_B = self.domain_B.bottom
        return ReducedProductAbstractState(bottom_A, bottom_B)

    def reduce(self, alpha):
        reduced_A = bilateral(self.domain_A, self.gamma_hat(alpha))
        reduced_B = bilateral(self.domain_B, self.gamma_hat(alpha))
        return ReducedProductAbstractState(reduced_A, reduced_B)

    def translate(self, translation):
        variables = list(map(translation.__getitem__, self.variables))
        domain_A = self.domain_A.translate(translation)
        domain_B = self.domain_B.translate(translation)
        return ReducedProductDomain(variables, domain_A, domain_B)
