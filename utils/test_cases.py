# -*- coding: utf8 -*- we should add test cases here because we can miss some cases while writing automation code or
# some manuel testers (test analystes) can handle this more efficiently we can obtain test cases from test management
#  tools, I used this for my previous project:
# http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx We can also record the result of test
# cases to test management tool

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array


def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to Login page, page should be loaded'],
    ['Blocker', 'In Welcome page, when user clicks on Companies & Contacts Tab, he should see Find/View page'],
    ['Blocker', 'In Main page, when user click "Sing up" button, he should see Sign up Page'],
    ['Blocker', 'In Main page, when user click "Sing in" button, he should see Sign in Page'],
    ['Blocker', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['Blocker', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
]
