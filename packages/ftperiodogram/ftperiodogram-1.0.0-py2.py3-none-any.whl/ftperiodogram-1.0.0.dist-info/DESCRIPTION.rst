
ftperiodogram package
=====================
`ftperiodogram` is a lightweight implementation of the fast template periodogram.
The fast template periodogram extends the [Lomb-Scargle]_ periodogram to arbitrary
signal shapes. It uses the nfft_ library to compute the non-equispaced fast Fourier
transform, and numpy_ and scipy_ libraries for other math-related computations.

For more information and links to usage examples, please see the
repository README_.

.. _README: https://github.com/PrincetonUniversity/FastTemplatePeriodogram/blob/master/README.md
.. _nfft: https://github.com/jakevdp/nfft
.. _numpy: https://www.numpy.org
.. _scipy: https://www.scipy.org
.. [Lomb-Scargle] http://docs.astropy.org/en/stable/stats/lombscargle.html

License
=======
`ftperiodogram` is licensed under the terms of the MIT license. See the file
"LICENSE.txt" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.


