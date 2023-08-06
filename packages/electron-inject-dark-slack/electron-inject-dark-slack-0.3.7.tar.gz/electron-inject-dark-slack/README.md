# electron-inject-slack-css

This is a fork of electron-inject it adds a dark theme to slack for people that want a dark theme.

Dark CSS for Slack created by https://github.com/Bigsy/dark-slack-theme (Modified to work with Desktop Slack).

*electron-inject-slack-css* uses electron-inject's javascript injection to load a custom css file into slack.


# install

	$ pip install electron-inject
	
	or

    $ python setup.py install
	
    
# usage

    $ python -m electron-inject-slack-css --help
    Usage:
        usage:
               electron-inject-slack-css [options] - <electron application>

        example:
               electron-inject-slack-css --enable-dev-tool-hotkey - /path/to/electron/powered/application [--app-params app-args]


    Options:
      -h, --help            show this help message and exit
      -d, --enable-devtools-hotkeys
                            Enable Hotkeys F12 (Toggle Developer Tools) and F5
                            (Refresh) [default: False]
	  -s  --enable-dark-slack-theme
							Enable Dark Theme for Slack. CSS file from 
							github.com/Bigsy/dark-slack-theme
      -t TIMEOUT, --timeout=TIMEOUT
                            Try hard to inject for the time specified [default:
                            none]
