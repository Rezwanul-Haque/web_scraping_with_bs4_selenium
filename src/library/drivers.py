class Drivers:
    pass


def CreatePhantomjsDriver(driver_path):
    try:
        from selenium import webdriver

        # create a phantom js driver
        PHANTOMJS_DRIVER = webdriver.PhantomJS(executable_path=driver_path)

        return PHANTOMJS_DRIVER

    except ImportError as exc:
        raise ImportError(
            "Couldn't import selenium. Are you sure it's installed them and "
            "Did you forget to activate a virtual environment?"
        ) from exc




