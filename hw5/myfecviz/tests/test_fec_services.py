from myfecviz.tests import FlaskClientTestCase
from myfecviz import get_db
from myfecviz.services import fec

from werkzeug.local import LocalProxy
import ujson

db = LocalProxy(get_db)

class FECServiceTest(FlaskClientTestCase):

    def test_get_number_of_candidates(self):
        """Verify number of candidates query."""
        self.assertEqual(5539, fec.get_number_of_candidates())

    def test_get_all_transaction_amounts_all_positive(self):
        """Verify all records returned are greater than 0."""
        results = fec.get_all_transaction_amounts()

        for result in results:
            self.assertLess(0, result['amount'])

    def test_get_all_transaction_amounts(self):
        """Verify the first dict has the right keys."""
        results = fec.get_all_transaction_amounts()
        result = results[0]

        # Inspect first result for proper keys
        self.assertIn('state', result)
        self.assertIn('amount', result)

    # def test_get_all_transaction_amounts_correct(self):
    #     """Verify the first dict has the right keys."""

    #     db.execute("SELECT transaction_amt, state FROM committee_contributions")
    #     whole_data = [dict(amount=float(row[0]), state=row[1]) for row in db.fetchall()]

    #     for record in whole_data:
    #         if record['amount'] > 0:
    #             self.assertIn('amount', result)


    #     results = fec.get_all_transaction_amounts()
    #     result = results[0]

    #     # Inspect first result for proper keys
    #     self.assertIn('state', result)
    #     self.assertIn('amount', result)    


    def test_get_total_transaction_amounts_by_state(self):
        """Verify transaction amount groupings have the right keys."""
        results = fec.get_total_transaction_amounts_by_state()

        result = results[0]
        self.assertIn('state', result)
        self.assertIn('total_amount', result)

    def test_get_total_transaction_amounts_all_positive(self):
        """Verify all records returned are greater than 0."""
        results = fec.get_total_transaction_amounts_by_state()

        for result in results:
            self.assertLess(0, result['total_amount'])
