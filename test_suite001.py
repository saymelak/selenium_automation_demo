from framework.elements import *
from framework.base_case import BaseCase
from nose.plugins.attrib import attr


class SmokeTestSuite002(BaseCase):

    @attr(priority="high")
    @attr(category="regression")
    def test_001_Should_be_able_to_navigate_through_all_pages_using_url(self):
        self.Open(Page.HOME)
        self.Verify().PageTitle('Home')

        self.Open(Page.TABLES)
        self.Verify().PageTitle('Tables')

        self.Open(Page.FORMS)
        self.Verify().PageTitle('Forms')

        self.Open(Page.MODALS)
        self.Verify().PageTitle('Modals')

        self.Open(Page.VARIOUS)
        self.Verify().PageTitle('Various components')

        self.Open(Page.CHARTS)
        self.Verify().PageTitle('Charts')

    @attr(priority="high")
    @attr(category="regression")
    def test_002_Should_be_able_to_navigate_through_all_pages_using_nav_bar(self):
        self.Navigate(To.HOME)
        self.Verify().PageTitle('Home')

        self.Navigate(To.TABLES)
        self.Verify().PageTitle('Tables')

        self.Navigate(To.FORMS)
        self.Verify().PageTitle('Forms')

        self.Navigate(To.MODALS)
        self.Verify().PageTitle('Modals')

        self.Navigate(To.VARIOUS)
        self.Verify().PageTitle('Various components')

        self.Navigate(To.CHARTS)
        self.Verify().PageTitle('Charts')

    @attr(priority="medium")
    @attr(category="sanity")
    def test_003_Should_be_able_to_add_contact(self):
        self.Navigate(To.FORMS)
        self.Send(Forms.NAME_FIELD, 'Rob Smith')
        self.Send(Forms.EMAIL_FIELD, 'rob.smith.com')
        self.Send(Forms.PASSWORD_FIELD, 'password123')
        self.Send(Forms.WEBSITE_FIELD, 'http://www.xyz.com')
        self.Send(Forms.PHONE_FIELD, '234-567-3434')
        self.Send(Forms.REFERENCE_FIELD, 'Facebook')
        self.Click(Forms.QUESTION_RADIO_BUTTON)
        self.Send(Forms.COMMENTS_FIELD, 'Comment 1, 2, 3, ...')
        self.Click(Forms.SEND_BUTTON)

        self.Verify().TextDisplayed(Forms.OUTPUT_TITLE, 'You have entered the following:')

    @attr(priority="low")
    @attr(category="smoke")
    def test_004_Should_be_able_to_display_charts(self):
        """ Navigate to the Charts Page """
        self.Navigate(To.CHARTS)

        """ Choose Line from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD, 'Line')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON)

        """ Verify that the Chart is displayed """
        self.Verify().CanvasSize(Charts.CHART1, 1072, 536)

        """ Choose Line from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD, 'Bar')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON)

        """ Verify that the Chart is displayed """
        self.Verify().CanvasSize(Charts.CHART1, 1072, 536)

        """ Choose Horizontal Bar from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD, 'Horizontal Bar')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON)

        """ Verify that the Chart is displayed """
        self.Verify().CanvasSize(Charts.CHART1, 1072, 536)

        """ Choose Doughnut from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD2, 'Doughnut')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON2)

        """ Verify that the Chart is displayed """
        self.Verify().CanvasSize(Charts.CHART1, 1072, 536)

        """ Choose Pie from the dropdown list """
        self.Select(Charts.CHART_TYPE_FIELD2, 'Pie')

        """ Click Submit """
        self.Click(Charts.SUBMIT_BUTTON2)

        """ Verify that the Chart is displayed """
        self.Verify().CanvasSize(Charts.CHART1, 1072, 536)

