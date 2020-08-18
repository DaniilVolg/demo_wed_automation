from random import randint

import pytest

index = randint(5, 5)
adress = '"{0}" Central park Racoon tree 1j NYC'.format(index)
name ="Kurt Maxx"
email = "kurtmaxx@gmail.com"

@pytest.fixture
def visit_site(py):
    py.visit("https://demoqa.com/text-box")


def test_submit_form_by_xpath(py, visit_site):
    py.getx("//input[@id='userName']").type(name)
    py.getx("//input[@id='userEmail']").type("kurtmaxx@gmail.com")
    py.getx("//textarea[@id='currentAddress']").type(first_address)
    py.getx("//textarea[@id='permanentAddress']").type(second_address)
    py.getx("//button[@id='submit']").click(force=True)
    output = py.get('#output')
    assert name in output.text()
    assert email in output.text()
    assert first_address in output.text()
    assert second_address in output.text()



