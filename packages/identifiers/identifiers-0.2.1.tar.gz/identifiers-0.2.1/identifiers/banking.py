# -*- coding: utf-8 -*-
##----------------------------------------------------------------------------
## Name:        banking
## Purpose:     International identifiers for banks and bank accounts
##
## Author:      Michael Amrhein (mamrhein@users.sourceforge.net)
##
## Copyright:   (c) 2016 Michael Amrhein
## License:     This program is part of a larger application. For license
##              details please read the file LICENSE.TXT provided together
##              with the application.
##----------------------------------------------------------------------------
## $Source: identifiers/banking.py $
## $Revision: 7bec0a7a54cc 2016-05-20 07:56 +0200 mamrhein $


"""International identifiers for banks and bank accounts"""


from __future__ import absolute_import, unicode_literals
from string import ascii_uppercase, digits
from iso3166 import countries
from .identifier import Identifier
from .ibanutils import get_iban_spec

str = type(u'')


__metaclass__ = type


_ALPHABET = digits + ascii_uppercase


class BIC(Identifier):

    """Business Identifier Code

    Used to identify financial and non-financial institutions.

    Each BIC consists of the Party Prefix (4 alpha-numeric), the
    Country Code (2 alpha) and the Party Suffix (2 alpha-numeric), optionally
    followed by the Branch Code (3 alpha-numeric).
    """

    __slots__ = ()

    @property
    def party_prefix(self):
        """Return the BIC's Party Prefix."""
        return self._id[:4]

    @property
    def country_code(self):
        """Return the BIC's Country Code."""
        return self._id[4:6]

    @property
    def party_suffix(self):
        """Return the BIC's Party Suffix."""
        return self._id[6:8]

    @property
    def branch_code(self):
        """Return the BIC's Branch Code (maybe empty)."""
        return self._id[8:]

    def elements(self):
        """Return the BIC's Party Prefix, Country Code, Party Suffix and
        Branch Code as a tuple."""
        return (self.party_prefix, self.country_code, self.party_suffix,
                self.branch_code)

    def __init__(self, bic):
        """
        Args:
            bic (`Unicode string`): string representation of the BIC

        Returns:
            :class:`BIC` instance

        Raises:
            TypeError: given `bic` is not a `Unicode string`
            ValueError: given `bic` (stripped) does not contain 8 or 11
                characters
            ValueError: given `bic` contains characters other than A-Z or 0-9
            ValueError: given `bic` contains an unknown country code
        """
        if not isinstance(bic, str):
            raise TypeError("Argument must be instance of %s." % str)
        bic = bic.strip()
        n_chars = len(bic)
        if n_chars not in (8, 11):
            raise ValueError("BIC must contain 8 or 11 characters.")
        msg = ''
        try:
            [_ALPHABET.index(char) for char in bic]
        except ValueError:
            msg = "BIC must only contain letters A-Z or digits."
        country_code = bic[4:6]
        try:
            countries.get(country_code)
        except KeyError:
            msg = ' '.join((msg,
                            "Unknown country code: '%s'." % country_code))
        if msg:
            raise ValueError(msg)
        self._id = bic

    def __str__(self):
        """str(self)"""
        return self._id


class IBAN(Identifier):

    """International Bank Account Number

    An internationally agreed system of identifying bank accounts across
    national borders.

    Each IBAN consists of a two-letter ISO 3166-1 Country Code, followed by
    two check digits and up to thirty alphanumeric characters for a BBAN
    (Basic Bank Account Number) which has a fixed length per country and,
    included within it, a bank identifier with a fixed position and a fixed
    length per country. The check digits are calculated based on the scheme
    defined in ISO/IEC 7064 (MOD97-10).
    """

    __slots__ = ()

    @staticmethod
    def calc_check_digits(country_code, bban):
        string = bban.upper() + country_code + '00'
        check_num = int(''.join((str(_ALPHABET.index(char))
                                 for char in string)))
        return '%02i' % (98 - check_num % 97)

    @property
    def country_code(self):
        """Return the IBAN's Country Code."""
        return self._id[:2]

    @property
    def check_digits(self):
        """Return the IBAN's check digits."""
        return self._id[2:4]

    @property
    def bank_identifier(self):
        """Return the IBAN's Bank Identifier."""
        end = get_iban_spec(self.country_code).bank_identifier_length + 4
        return self._id[4:end]

    @property
    def bank_account_number(self):
        """Return the IBAN's Bank Account Number."""
        start = get_iban_spec(self.country_code).bank_identifier_length + 4
        return self._id[start:]

    def elements(self):
        """Return the IBAN's Country Code, check digits, Bank Identifier and
        Bank Account Number as tuple."""
        return (self.country_code, self.check_digits, self.bank_identifier,
                self.bank_account_number)

    def __init__(self, *args):
        """Instances of :class:`IBAN` can be created in two ways, by providing
        a Unicode string representation of an IBAN or by providing a country
        code, a bank identifier and a bank account number.

        **1. Form**

        Args:
            iban (`Unicode string`): string representation of an IBAN

        Returns:
            instance of :class:`IBAN`

        Raises:
            TypeError: given `iban` is not a `Unicode string`
            ValueError: given `iban` contains an unknown country code
            ValueError: given `iban` contains wrong check digits
            ValueError: given `iban` does not follow the format required for
                the given country code

        **2. Form**

        Args:
            country_code (`Unicode string`): 2-character country code
                according to ISO 3166
            bank_identifier (`Unicode string` or `int`): code identifying the
                bank maintaining the account
            bank_account_number (`Unicode string` or `int`): code identifying
                the account (within the namespace of the bank)

        Returns:
            instance of :class:`IBAN`

        Raises:
            TypeError: invalid number of arguments
            TypeError: given `country_code` is not a `Unicode string`
            ValueError: given `country_code` contains an invalid or unknown
                country code
            TypeError: given `bank_identifier` is not a `Unicode string` or
                not an `int`
            ValueError: length of given `bank_identifier` not valid for
                the given country code
            TypeError: given `bank_account_number` is not a `Unicode string`
                or not an `int`
            ValueError: length of given `bank_account_number` not valid for
                the given country code
            ValueError: given `bank_identifier` and `bank_account_number` do
                not follow the BBAN format required for the given country code
        """
        n_args = len(args)
        if n_args == 1:
            arg0 = args[0]
            if not isinstance(arg0, str):
                raise TypeError("Argument must be instance of %s." % str)
            arg0 = arg0.strip()
            country_code = arg0[:2]
            try:
                bban_length, bban_structure, bank_identifier_length, _ = \
                    get_iban_spec(country_code)
            except KeyError:
                raise ValueError("Unknown country code: '%s'." % country_code)
            bban = arg0[4:]
            if len(bban) == bban_length and bban_structure.match(bban):
                check_digits = self.__class__.calc_check_digits(country_code,
                                                                bban)
                if check_digits != arg0[2:4]:
                    raise ValueError("Wrong check digits; should be '" +
                                     check_digits + "'.")
                self._id = arg0
            else:
                raise ValueError('Invalid IBAN format.')
        elif n_args == 3:
            arg0 = args[0]
            if not isinstance(arg0, str):
                raise TypeError("Country code must be instance of %s." % str)
            if len(arg0) != 2:
                raise ValueError("Country code must be a 2-character string.")
            country_code = arg0
            try:
                bban_length, bban_structure, bank_identifier_length, _ = \
                    get_iban_spec(country_code)
            except KeyError:
                raise ValueError("Unknown country code: '%s'." % country_code)
            arg1 = args[1]
            if isinstance(arg1, str):
                if len(arg1) == bank_identifier_length:
                    bank_identifier = arg1
                else:
                    raise ValueError("Bank identifier, if given as a string, "
                                     "must contain %i chars."
                                     % bank_identifier_length)
            elif isinstance(arg1, int):
                bank_identifier = format(arg1,
                                         '0%id' % bank_identifier_length)
                if len(bank_identifier) != bank_identifier_length:
                    raise ValueError("Bank identifier, if given as an int, "
                                     "must not have more than %i digits."
                                     % bank_identifier_length)
            else:
                raise TypeError("Bank identifier must be instance of "
                                "%s or %s." % (str, int))
            arg2 = args[2]
            account_number_length = bban_length - bank_identifier_length
            if isinstance(arg2, str):
                if len(arg2) == account_number_length:
                    bank_account_number = arg2
                else:
                    raise ValueError("Bank account number, if given as a "
                                     "string, must contain %i chars."
                                     % account_number_length)
            elif isinstance(arg2, int):
                bank_account_number = format(arg2,
                                             '0%id' % account_number_length)
                if len(bank_account_number) != account_number_length:
                    raise ValueError("Bank account number, if given as an "
                                     "int, must not have more than %i digits."
                                     % bank_identifier_length)
            else:
                raise TypeError("Bank account number must be instance of "
                                "%s or %s." % (str, int))
            bban = bank_identifier + bank_account_number
            if bban_structure.match(bban):
                check_digits = self.__class__.calc_check_digits(country_code,
                                                                bban)
                self._id = ''.join((country_code, check_digits,
                                    bank_identifier, bank_account_number))
            else:
                raise ValueError('Invalid IBAN format.')
        else:
            raise TypeError('Invalid number of arguments.')

    def __str__(self):
        """str(self)"""
        return ' '.join((self._id[i:i + 4]
                         for i in range(0, len(self._id), 4)))
