def test_radio_button_shows_yes(py):
    py.visit("https://demoqa.com/radio-button")
    py.getx("//label[contains(text(),'Yes')]").click()
    assert py.getx("//label[contains(text(),'Yes')]").should().contain_text("Yes")


def test_impessive_radio_button_is_selected(py):
    py.visit("https://demoqa.com/radio-button")
    checkbox =py.get("#impressiveRadio")
    checkbox.click(force=True)
    assert checkbox.should().be_selected()

def test_inject_javascript_elements_to_enable_radio_buttons(py):

    py.visit("https://demoqa.com/radio-button")
    no_square= py.get("#noRadio")
    py.execute_script("arguments[0].disabled=false",no_square.webelement)
    no_square.click(force=True)
    assert no_square.is_selected()
