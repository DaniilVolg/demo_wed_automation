def test_submit_form_by_xpath(py):
    py.visit("https://demoqa.com/text-box")
    py.getx("//input[@id='userName']").type("Kurt Maxx")
    py.getx("//input[@id='userEmail']").type("kurtmaxx@gmail.com")
    py.getx("//textarea[@id='currentAddress']").type("11230 Central park ,Racoon tree 1j ,NYC ")
    py.getx("//textarea[@id='permanentAddress']").type("Same")
    py.getx("//button[@id='submit']").click(force=True)
    assert py.getx("//p[@id='name']").should().contain_text("Kurt Maxx")


def test_submit_form_by_Css(py):
    py.visit("https://demoqa.com/text-box")
    py.get("#userName").type("Kurt Maxx")
    py.get("#userEmail").type("kurtmaxx@gmail.com")
    py.get("#currentAddress").type("11230 Central park ,Racoon tree 1j ,NYC ")
    py.get("#permanentAddress").type("Same")
    py.get("#submit").click(force=True)
    assert py.get('p[id="name"]').should().contain_text("Kurt Maxx")
