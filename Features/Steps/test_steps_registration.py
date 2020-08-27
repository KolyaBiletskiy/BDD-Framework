from behave import given, when, then, parser

@given(u'User is on registration page')
def step_impl(context):
    context.driver.get('http://www.thetestingworld.com/testings')


@when(u'user enters username')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys('username')


@when(u'user enters email id')
def step_impl(context):
    context.driver.find_element_by_name('fld_email').send_keys('username@us.us')


@when(u'user enters password')
def step_impl(context):
    context.driver.find_element_by_name('fld_password').send_keys('12321321')


@when(u'user clock on signup button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Sign up']").click()


@then(u'user should be registered successfully')
def step_impl(context):
    print('Registered')

@then(u'user should not be registered successfully')
def step_impl(context):
    print('Not Registered')