import allure
import pytest

from models.customer import CreateCustomer
from pages.try_sql_page import TrySQLPage, TrySQLPageResultColumn
from utils.constants.features import Feature
from utils.constants.routes import UIRoutes
from utils.constants.suites import Suite


@pytest.mark.ui
@pytest.mark.customers_sql
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite(Suite.SMOKE)
@allure.feature(Feature.CUSTOMERS)
class TestSearch:
    SQL_TRYSQL_URL = f'{UIRoutes.SQL_TRYSQL}?filename=trysql_select_all'
    @allure.id('1')
    @allure.title('Select all customers')
    @pytest.mark.parametrize('text', ['Via Ludovico il Moro 22'])
    @pytest.mark.parametrize('reference_text', ['Via Ludovico il Moro 22'])
    def test_select_all_customers(self, try_sql_page: TrySQLPage, text: str, reference_text: str):
        try_sql_page.visit(self.SQL_TRYSQL_URL)
        # try_sql_page.fill_sql_editor('SELECT * FROM Customers;')
        # try_sql_page.run_sql()
        # try_sql_page.check_result_table_data(
        #     expected_text=text,
        #     reference_text=reference_text,
        #     column=TrySQLPageResultColumn.ADDRESS
        # )