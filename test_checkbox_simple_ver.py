import time


def test_checkbox(py):
    py.visit("https://demoqa.com/checkbox")
    parent_checkbox = py.getx("//button[@class='rct-collapse rct-collapse-btn']//*[local-name()='svg']").click()
    time.sleep(5)
    child_box_downloads = py.getx("//li[3]//span[1]//button[1]//*[local-name()='svg']").click()
    time.sleep(5)
    grand_child_word = py.getx("//body//li[@class='rct-node rct-node-parent rct-node-expanded']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[1]//span[1]//label[1]//span[1]//*[local-name()='svg']").click()
    time.sleep(5)
    success = py.getx("//span[@class='text-success']")
    assert success.should().contain_text("wordFile")
