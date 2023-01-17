const { Builder, By, Key, until } = require("selenium-webdriver");

describe("Selenium 'Hello world'", () => {
  let driver;
  beforeAll(() => {
    driver = new Builder().forBrowser("chrome").build();
  });

  afterAll(() => {
    setTimeout(() => {
      driver.quit();
    }, 2000);
  });

  it("Should open Inkarnate", async () => {
    await driver.get("https://inkarnate.com/");
    driver.getTitle().then((title) => {
      expect(title).toContain("Inkarnate");
    });
  });

  it("Should click on 'Explore the free version & tanke to sing up'", async () => {
    await driver.get("https://inkarnate.com/");
    const element = await driver.executeScript(function () {
      return Array.from(document.getElementsByTagName("a")).find(
        (element) => element.innerHTML == "Explore the free version"
      );
    });
    await element.sendKeys("selenium", Key.RETURN);
    await driver.wait(until.titleContains("Inkarnate"), 4000);
    driver.getTitle().then((title) => {
      expect(title).toEqual("Sign up | Inkarnate - Create Fantasy Maps Online");
    });
  });
});
