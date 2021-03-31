def cases(number):
    return Cases[number]


Cases = [
    # [severity, description]
    ['Blocker', 'when user goes to Login page, page should be loaded'],
    ['Blocker', 'In Welcome page, when user clicks on Companies & Contacts Tab, he should see Find/View page'],
    ['Blocker', 'In Main page, when user click "Sing up" button, he should see Sign up Page'],
    ['Blocker', 'In Main page, when user click "Sing in" button, he should see Sign in Page'],
    ['Blocker', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['Blocker', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
]
