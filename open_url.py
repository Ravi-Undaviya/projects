import webbrowser
import urllib.request
# get searching keyword from the user
search = input('Google search: ')
# open link in new tab of your default browser
webbrowser.open_new_tab('https://google.com/search?btnG=1&q=%s' % search)
