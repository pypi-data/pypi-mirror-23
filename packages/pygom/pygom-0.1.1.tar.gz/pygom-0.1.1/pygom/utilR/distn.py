"""
    .. moduleauthor:: Edwin Tye <Edwin.Tye@phe.gov.uk>

    Functions of distributions that replicate those in R.
    See the R online documentation for each of the functions
    with matching names, i.e. dgamma, pgamma and rgamma
    can be found at
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html

"""

import scipy.stats
import numpy as np

###############################################################
#
# Continuous distribution
#
###############################################################

##### exponential distribution

def dexp(x, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html
    '''
    if log:
        return scipy.stats.expon.pdf(x, scale=1.0/rate)
    else:
        return scipy.stats.expon.pdf(x, scale=1.0/rate)

def pexp(q, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html
    '''
    if log:
        return scipy.stats.expon.logcdf(q, scale=1.0/rate)
    else:
        return scipy.stats.expon.cdf(q, scale=1.0/rate)

def qexp(p, rate=1.0):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html
    '''
    return scipy.stats.expon.ppf(p, scale=1.0/rate)

def rexp(n, rate=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html
    
    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    rvs = scipy.stats.expon.rvs
    if seed is True: 
        rvs = np.random.RandomState().exponential
    elif isinstance(seed, np.random.RandomState):
        rvs = seed.exponential
    elif isinstance(seed, int):
        np.random.seed(seed)

    if n > 1:
        return rvs(scale=1.0/rate, size=n)
    else:
        return rvs(scale=1.0/rate, size=n)[0]


##### gamma distribution

def dgamma(x, shape, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html
    '''
    if log:
        return scipy.stats.gamma.logpdf(x, a=shape, scale=1.0/rate)
    else:
        return scipy.stats.gamma.pdf(x, a=shape, scale=1.0/rate)

def pgamma(q, shape, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html
    '''
    if log:
        return scipy.stats.gamma.logcdf(q, a=shape, scale=1.0/rate)
    else:
        return scipy.stats.gamma.cdf(q, a=shape, scale=1.0/rate)

def qgamma(q, shape, rate=1.0):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html
    '''
    return scipy.stats.gamma.ppf(q, a=shape, scale=1.0/rate)
    
def rgamma(n, shape, rate=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    rvs = scipy.stats.gamma.rvs
    if seed is True: 
        rvs = np.random.RandomState().gamma
    elif isinstance(seed, np.random.RandomState):
        rvs = seed.gamma
    elif isinstance(seed, int):
        np.random.seed(seed)
        
    if n > 1:
        return rvs(shape, scale=1.0/rate, size=n)
    else:
        return rvs(shape, scale=1.0/rate, size=n)[0]

##### normal distribution

def dnorm(x, mean=0, sd=1, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html
    '''
    if log:
        return scipy.stats.norm.logpdf(x, loc=mean, scale=sd)
    else:
        return scipy.stats.norm.pdf(x, loc=mean, scale=sd)

def pnorm(q, mean=0, sd=1, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html
    '''
    if log:
        return scipy.stats.norm.logcdf(q, loc=mean, scale=sd)
    else:
        return scipy.stats.norm.cdf(q, loc=mean, scale=sd)

def qnorm(p, mean=0, sd=1):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html
    '''
    return scipy.stats.norm.ppf(p, loc=mean, scale=sd)
    
def rnorm(n, mean=0, sd=1, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used.  If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly 
    '''
    rvs = scipy.stats.norm.rvs
    if seed is True: 
        rvs = np.random.RandomState().normal
    elif isinstance(seed, np.random.RandomState):
        rvs = seed.normal
    elif isinstance(seed, int):
        np.random.seed(seed)
        
    if n > 1:
        return rvs(loc=mean, scale=sd, size=n)
    else:
        return rvs(loc=mean, scale=sd, size=n)[0]

##### Chi-squared distribution

def dchisq(x, df, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    '''
    if log:
        return scipy.stats.chi2.logpdf(x, df=df)
    else:
        return scipy.stats.norm.pdf(x, df=df)

def pchisq(x, df, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    '''
    if log:
        return scipy.stats.chi2.logpdf(x, df=df)
    else:
        return scipy.stats.chi2.pdf(x, df=df)  

def qchisq(p, df):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    '''
    return scipy.stats.chi2.ppf(p, df=df)

def rchisq(n, df, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    
    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    rvs = scipy.stats.chi2.rvs
    if seed is True: 
        rvs = np.random.RandomState().chisquare
    elif isinstance(seed, np.random.RandomState):
        rvs = seed.chisquare
    elif isinstance(seed, int):
        np.random.seed(seed)
        
    if n > 1:
        return rvs(df=df, size=n)
    else:
        return rvs(df=df, size=n)[0]

##### Uniform distribution

def dunif(x, min=0.0, max=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html
    '''
    if log:
        return scipy.stats.uniform.logpdf(x, loc=min, scale=max-min)
    else:
        return scipy.stats.uniform.pdf(x, loc=min, scale=max-min)

def punif(q, min=0.0, max=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html
    '''
    if log:
        return scipy.stats.uniform.logcdf(q, loc=min, scale=max-min)
    else:
        return scipy.stats.uniform.cdf(q, loc=min, scale=max-min)
    
def qunif(p, min=0.0, max=1.0):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html
    '''
    return scipy.stats.uniform.ppf(p, loc=min, scale=max-min)    

def runif(n, min=0.0, max=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html
    
    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is True: 
        rvs = np.random.RandomState().uniform
    elif isinstance(seed, np.random.RandomState):
        rvs = seed.uniform
    elif isinstance(seed, int):
        np.random.seed(seed)
    
    if seed:
        if n > 1:
            return scipy.stats.uniform.rvs(loc=min, scale=max-min, size=n)
        else:
            return scipy.stats.uniform.rvs(loc=min, scale=max-min, size=n)[0]
    else:
        if n > 1:
            return rvs(low=min, high=max, size=n)
        else:
            return rvs(low=min, high=max, size=n)[0]

###############################################################
#
# Discrete distribution
#
###############################################################

##### Poisson distribution

def dpois(x, mu=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html
    '''
    if log:
        return scipy.stats.poisson.logpmf(x, mu=mu)
    else:
        return scipy.stats.poisson.pmf(x, mu=mu)

def ppois(q, mu=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html
    '''
    if log:
        return scipy.stats.poisson.logcdf(q, mu=mu)
    else:
        return scipy.stats.poisson.cdf(q, mu=mu)

def qpois(q, mu=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html
    '''
    return scipy.stats.poisson.ppf(q, mu=mu)
    
def rpois(n, mu=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly 
    '''
    rvs = scipy.stats.poisson.rvs
    if seed is True: 
        rvs = np.random.RandomState().poisson
    elif isinstance(seed, np.random.RandomState):
        rvs = seed.poisson
    elif isinstance(seed, int):
        np.random.seed(seed)
        
    if n > 1:
        return rvs(mu, size=n)
    else:
        return rvs(mu, size=n)[0]

##### Binomial distribution

def dbinom(x, size, prob, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html
    '''
    if log:
        return scipy.stats.binom.logpmf(x, n=size, p=prob)
    else:
        return scipy.stats.binom.pmf(x, n=size, p=prob)

def pbinom(q, size, prob, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html
    '''
    if log:
        return scipy.stats.binom.logcdf(q, n=size, p=prob)
    else:
        return scipy.stats.binom.cdf(q, n=size, p=prob)

def qbinom(q, size, prob):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html
    '''
    return scipy.stats.binom.ppf(q, n=size, p=prob)
    
def rbinom(n, size, prob, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    rvs = scipy.stats.binom.rvs
    if seed is True: 
        rvs = np.random.RandomState().binomial
    elif isinstance(seed, np.random.RandomState):
        rvs = seed.binomial
    elif isinstance(seed, int):
        np.random.seed(seed)
    
    if n > 1:
        return rvs(n=size, p=prob, size=n)
    else:
        return rvs(n=size, p=prob, size=n)[0]
