#!/usr/bin/env python

# Background color for labels
from colorama import Fore, Back, Style, init
import json
from datetime import datetime
import pydoc
import requests
import argparse
import sys
import time
import os.path

try:
    import configparser
except:
    from six.moves import configparser

def get_args(argv=None):
	file_path = set_configuration()
	conf = configparser.SafeConfigParser()

	conf.read(file_path)
	user = conf.get('GitHub Newsfeed', 'user')
	max_page = conf.get('GitHub Newsfeed', 'max_page')
	quiet = conf.get('GitHub Newsfeed', 'quiet')
	no_time_stamp = conf.get('GitHub Newsfeed', 'no_time_stamp')
	no_style = conf.get('GitHub Newsfeed', 'no_style')

	parser = argparse.ArgumentParser(description='Check your GitHub Newsfeed via the command-line.',
	                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-u', '--user', default=user,
	                    help='GitHub username for the user to fetch newsfeed for')
	parser.add_argument('-p', '--pages', default=max_page,
	                    help='number of newsfeed pages to fetch')
	parser.add_argument('-q', '--quiet', default=False,
	                    help='hide comment body in issues & PRs', action='store_true')
	parser.add_argument('-nt', '--no-time-stamp', default=False,
	                    help='hide time-stamp of events', action='store_true')
	parser.add_argument('-ns', '--no-style', default=False,
	                    help='show plain white text with no colors or style', action='store_true')
	return parser.parse_args(sys.argv[1:])

def set_configuration():
	conf = configparser.SafeConfigParser()

	home = os.path.expanduser('~')
	folder_name = '.gitfeed'
	folder_path = os.path.join(home, folder_name)

	if not os.path.exists(folder_path):
		os.makedirs(folder_path)

	file_name = 'gitfeed.ini'
	file_path = os.path.join(home, folder_name, file_name)

	if not os.path.isfile(file_path):
		if sys.version_info > (3,0):
			user = input("What's your GitHub username? ")
		else:
			user = raw_input("What's your GitHub username? ")
		print('Writing configuration to ' + file_path)
		conf.add_section('GitHub Newsfeed')
		conf.set('GitHub Newsfeed', 'user', user)
		conf.set('GitHub Newsfeed', 'max_page', '1')
		conf.set('GitHub Newsfeed', 'quiet', 'False')
		conf.set('GitHub Newsfeed', 'no_time_stamp', 'False')
		conf.set('GitHub Newsfeed', 'no_style', 'False')

		with open(file_path, 'w') as configfile:
			conf.write(configfile)
		print('')

	return file_path

def remove_color():
	Fore.GREEN = ''
	Fore.CYAN = ''
	Fore.RED = ''
	Fore.YELLOW = ''
	Fore.MAGENTA = ''
	Fore.BLUE = ''
	Fore.WHITE = ''
	Style.BRIGHT = ''
	Back.BLUE = ''
	return

def fix_encoding(query):
	if sys.version_info > (3, 0):
		return query
	else:
		return query.encode('utf-8')

# review PR
def PRReviewEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	#commit = item['payload']['comment']['commit_id']
	#link = item['payload']['pull_request']['html_url']
	#title = item['payload']['pull_request']['title']
	number = item['payload']['pull_request']['number']
	body = item['payload']['comment']['body']

	event_output = [fix_encoding(Fore.CYAN + Style.BRIGHT + '{} reviewed pull request {} on {}'.format(user, number, repo))]
	if not quiet:
		event_output.append(fix_encoding(body))

	return "\n".join(event_output)

# open PR, close PR
def PREvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = item['payload']['pull_request']['html_url']
	state = item['payload']['pull_request']['state']
	number = item['payload']['pull_request']['number']
	title = item['payload']['pull_request']['title']

	event_output = []
	if state == 'open':
		event_output.append(fix_encoding(Fore.CYAN + '{} opened pull request {} on {}'.format(user, number, repo)))
		event_output.append(fix_encoding(Style.BRIGHT + fix_encoding(title)))
		body = item['payload']['pull_request']['body']
		if not quiet and not body is None:
			event_output.append(fix_encoding(body))
	else:
		event_output.append(fix_encoding(Fore.CYAN + '{} closed pull request {} on {}'.format(user, number, repo)))
		event_output.append(fix_encoding(Style.BRIGHT + title))

	return "\n".join(event_output)

# comment on issue, PR
def issueCommentEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = item['payload']['issue']['html_url']
	#labels = item['payload']['issue']['labels'] # FIX_ME
	#for x in labels:
	#	print(x['name'])
	#state = item['payload']['action']
	number = item['payload']['issue']['number']
	#title = item['payload']['issue']['title']
	try:
		if item['payload']['issue']['pull_request']:
			group = 'pull request'
	except:
		group = 'issue'

	event_output = [fix_encoding(Fore.CYAN + Style.BRIGHT + '{} commented on {} {} on {}'.format(user, group, number, repo))]
	if not quiet:
		body = item['payload']['comment']['body']
		event_output.append(fix_encoding(body))

	return "\n".join(event_output)

# open issue, close issue
def issuesEvent(item):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = item['payload']['issue']['html_url']
	state = item['payload']['action']
	number = item['payload']['issue']['number']

	event_output = [fix_encoding(Fore.RED + Style.BRIGHT + '{} {} issue {} on {}'.format(user, state, number, repo))]
	title = item['payload']['issue']['title']
	event_output.append(fix_encoding(Style.BRIGHT + title))

	return "\n".join(event_output)

# comment on a commit
def commitCommentEvent(item, quiet):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = item['payload']['issue']['html_url']
	body = item['payload']['comment']['body']

	event_output = [fix_encoding(Fore.CYAN + Style.BRIGHT + '{} commented on {}'.format(user, repo))]
	if not quiet:
		event_output.append(fix_encoding(body))

	return "\n".join(event_output)

# starred by following
def watchEvent(item):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = 'https://github.com/' + item['repo']['name']
	event_output = fix_encoding(Fore.YELLOW + '{} starred {}'.format(user, repo))
	return event_output

# forked by following
def forkEvent(item):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = 'https://github.com/' + item['repo']['name']
	event_output = fix_encoding(Fore.GREEN + '{} forked {}'.format(user, repo))
	return event_output

# delete branch
def deleteEvent(item):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = 'https://github.com/' + item['repo']['name']
	branch = item['payload']['ref']

	event_output = fix_encoding(Fore.RED + '{} deleted branch {} at {}'.format(user, branch, repo))
	return event_output

# push commits
def pushEvent(item):
	user = item['actor']['login']
	size = item['payload']['size']
	repo = item['repo']['name']
	branch = item['payload']['ref'].split('/')[-1]
	#link = 'https://github.com/' + item['repo']['name']

	event_output = fix_encoding(Fore.BLUE + '{} pushed {} new commit(s) to {} at {}'.format(user, size, branch, repo))
	return event_output

# create repo, branch
def createEvent(item):
	user = item['actor']['login']
	repo = item['repo']['name']
	group = item['payload']['ref_type']
	#link = 'https://github.com/' + item['repo']['name']

	event_output = ""
	if group == "repository":
		event_output = fix_encoding(Fore.MAGENTA + Style.BRIGHT + '{} created {} {}'.format(user, group, repo))
	else:
		branch = item['payload']['ref']
		event_output = fix_encoding(Fore.MAGENTA + Style.BRIGHT + '{} created {} {} at {}'.format(user, group, branch, repo))

	return event_output

# make public repo
def publicEvent(item):
	user = item['actor']['login']
	repo = item['repo']['name']
	#link = 'https://github.com/' + item['repo']['name']

	event_output = fix_encoding(Fore.MAGENTA + '{} made {} public'.format(user, repo))
	return event_output

# add collab
def memberEvent(item):
	user = item['actor']['login']
	action = item['payload']['action']
	collab = item['payload']['member']['login']
	repo = item['repo']['name']
	#link = 'https://github.com/' + item['repo']['name']

	event_output = fix_encoding(Fore.MAGENTA + '{} {} {} as a collaborator to {}'.format(user, action, collab, repo))
	return event_output

def get_time_difference(created_at):
	created_at = time.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
	created_at = time.mktime(created_at)

	current_time = datetime.utcnow().replace(microsecond=0)
	current_time = current_time.isoformat() + 'Z'
	current_time = time.strptime(current_time, '%Y-%m-%dT%H:%M:%SZ')
	current_time = time.mktime(current_time)

	difference = current_time - created_at

	days = ('day', int(int(difference) / 86400))
	hours = ('hour', int(int(difference) / 3600 % 24))
	minutes = ('minute', int(int(difference) / 60 % 60))
	seconds = ('second', int(int(difference) % 60))

	human_readable = (seconds, minutes, hours, days)
	for item in human_readable:
		if not item[1] == 0:
			if item [1] == 1:
				statement = '{} {} ago'.format(item[1], item[0])
			else:
				statement = '{} {}s ago'.format(item[1], item[0])

	return statement

def get_page(user, page, quiet, nt):
	url = 'https://api.github.com/users/' + user +'/received_events?page='
	response = json.loads(requests.get(url + str(page)).text)
	output = []
	for item in response:
		if not nt:
			created_at = item['created_at']
			difference = get_time_difference(created_at)

			#print(Fore.WHITE + Style.NORMAL + Back.BLUE + difference)
			output.append(Fore.WHITE + Back.BLUE + difference + Back.RESET)

		event = item['type']

		if event == "PullRequestReviewCommentEvent": # review PR
			output.append(PRReviewEvent(item, quiet))
		elif event == "PullRequestEvent": # open PR, close PR
			output.append(PREvent(item, quiet))
		elif event == "IssueCommentEvent": # comment on issue/PR
			output.append(issueCommentEvent(item, quiet))
		elif event == "IssuesEvent": # open issue, close issue
			output.append(issuesEvent(item))
		elif event == "CommitCommentEvent":
			output.append(commitCommentEvent(item, quiet))
		elif event == "WatchEvent": # starred
			output.append(watchEvent(item))
		elif event == "ForkEvent": # fork
			output.append(forkEvent(item))
		elif event == "DeleteEvent": # delete branch
			output.append(deleteEvent(item))
		elif event == "PushEvent": # push commits
			output.append(pushEvent(item))
		elif event == "CreateEvent": # make new repo, branch
			output.append(createEvent(item))
		elif event == "PublicEvent": # make repo public
			output.append(publicEvent(item))
		elif event == "MemberEvent": # add collab
			output.append(memberEvent(item))

		output.append("")
	return "\n".join(output)

def get_pages(user, max_page, quiet, nt):
	output = []
	for page in range(1, max_page+1):
		output.append(get_page(user, page, quiet, nt))

	pydoc.pager("\n".join(output))

def cli():
	init(autoreset=True)

	args = get_args()
	user = args.user
	max_page = int(args.pages)
	quiet = args.quiet
	nt = args.no_time_stamp

	if args.no_style:
		remove_color()

	get_pages(user, max_page, quiet, nt)

if __name__ == '__main__':
	cli()
