Chrome = {
    'browserName': 'chrome',
    'chromeOptions': { 'args': [
        '--no-sandbox',
        # '--headless',
        '--disable-gpu',
        '--start-maximized',
        '--disable-infobars',
        '--disable-extensions',
        '--enable-logging --v=1',
        '--window-size=1920,1080',
    ]
    }
}