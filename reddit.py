#Name : Aileena Xie
#Student ID: 261050876

import praw
import time
import random
from madlibs import *

def get_topic_comments(submission):
    '''(Submission) -> list
    Returns a list of all Comment objects that are contained in submission
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/eay2ne/mcgill_subreddit_bingo_finals_edition/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='fb0vh26'), Comment(id='fb0l4dk'), Comment(id='fb15bvy'),
    Comment(id='fb1pwq8'), Comment(id='fb26drr'), Comment(id='i1fcjed'),
    Comment(id='fj2wd6x'), Comment(id='i11plzg'), Comment(id='i1fcjwz'),
    Comment(id='fb1spzv'), Comment(id='fb1td2g'), Comment(id='fb1trul')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/moxbw2/cats/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='f487wgp'), Comment(id='f488nrl'), Comment(id='f489jjy'),
    Comment(id='f489wx8'), Comment(id='f48cl0w'), Comment(id='f48fmdy'),
    Comment(id='f48g8fy'), Comment(id='f4aysam'), Comment(id='f4bai22'),
    Comment(id='f48cfo2'), Comment(id='f4igym0'), Comment(id='f499cut'),
    Comment(id='f4bovhv'), Comment(id='f48krrx'), Comment(id='f4bjxn1'),
    Comment(id='f4anqrm'), Comment(id='f4ax2xn'), Comment(id='f4bvzsp'),
    Comment(id='f4jvc18'), Comment(id='f4bouej'), Comment(id='f4botlv'),
    Comment(id='f48kko0'), Comment(id='f48tjyi'), Comment(id='f4c8vbp'), Comment(id='f4car3h')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/djtpmb/cat_on_campus/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='f487wgp'), Comment(id='f488nrl'), Comment(id='f489jjy'),
    Comment(id='f489wx8'), Comment(id='f48cl0w'), Comment(id='f48fmdy'),
    Comment(id='f48g8fy'), Comment(id='f4aysam'), Comment(id='f4bai22'),
    Comment(id='f48cfo2'), Comment(id='f4igym0'), Comment(id='f499cut'),
    Comment(id='f4bovhv'), Comment(id='f48krrx'), Comment(id='f4bjxn1'),
    Comment(id='f4anqrm'), Comment(id='f4ax2xn'), Comment(id='f4bvzsp'),
    Comment(id='f4jvc18'), Comment(id='f4bouej'), Comment(id='f4botlv'),
    Comment(id='f48kko0'), Comment(id='f48tjyi'), Comment(id='f4c8vbp'), Comment(id='f4car3h')]
    
    '''
    
    submission.comments.replace_more(limit=100)  #To avoid rate limit error
    return submission.comments.list()



def filter_comments_from_authors(comments, authors_list):
    '''(Comments, list) -> list
    Returns a list containing comments that were written by authors
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['Juan_Carl0s', 'Chicken_Nugget31'])
    [Comment(id='ha4piat'), Comment(id='ha4j1r7')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/moxbw2/cats/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments,['Magicshop_21'])
    [Comment(id='gu7kgsn'), Comment(id='gu7kxjs'), Comment(id='gu7ld3m')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/djtpmb/cat_on_campus/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['nazaz', 'confusedsamosa', 'lexicries'])
    [Comment(id='f4bovhv'), Comment(id='f4bouej'), Comment(id='f4botlv'), Comment(id='f48krrx'), Comment(id='f4igym0')]
    
    '''
    
    filtered_list = []
    
    for author in authors_list:
        for comment in comments:
            if comment.author == author:     
                filtered_list.append(comment)
    
    return filtered_list
        
        
   

def filter_out_comments_replied_to_by_authors(comments, authors_list):
    '''(Comment, list) -> list
    Returns comments_list without the comments which have been replied to by any of the authors
    in authors_list and without the comments written by the authors in authors_list
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/qo5qd4/cat_chasing_birds_outside_of_mcconnell_today_what/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['ChickenMcChickenFace', 'mb4v', 'boom_boom_kachow'])
    [Comment(id='hjl15k6'), Comment(id='hjl3f1y'), Comment(id='hjkx7zc'), Comment(id='hjljj20'),
    Comment(id='hjkwe7n'), Comment(id='hjkwiwn'), Comment(id='hjkymxc'), Comment(id='hjkwf6f'),
    Comment(id='hjoz2za'), Comment(id='hjlz9im'), Comment(id='hjkv68f'), Comment(id='hjl8d9e'),
    Comment(id='hjl26eh'), Comment(id='hjl3hc2'), Comment(id='hjp403t'), Comment(id='hjoy5h7'),
    Comment(id='hjkyxfy'), Comment(id='hjlz0gp'), Comment(id='hjl2zyd'), Comment(id='hjlpgjs'),
    Comment(id='hjm0r63'), Comment(id='hjl0qgz'), Comment(id='hjl5n9n'), Comment(id='hjlqofw')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/moxbw2/cats/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['sersaretheproduct', 'Peakedinhsgang'])
    [Comment(id='gu6vw79'), Comment(id='gu6vbc8'), Comment(id='gu879g5'), Comment(id='gu7ddlc'),
    Comment(id='gu82ha5'), Comment(id='gueca3q'), Comment(id='gu9yy6l'), Comment(id='gu7ld3m')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/djtpmb/cat_on_campus/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['nazaz', 'damanas'])
    [Comment(id='f487wgp'), Comment(id='f489wx8'), Comment(id='f48cl0w'),
    Comment(id='f48fmdy'), Comment(id='f48g8fy'), Comment(id='f4aysam'),
    Comment(id='f4bai22'), Comment(id='f48cfo2'), Comment(id='f4igym0'),
    Comment(id='f499cut'), Comment(id='f4bjxn1'), Comment(id='f4anqrm'),
    Comment(id='f4ax2xn'), Comment(id='f4bvzsp'), Comment(id='f4jvc18'),
    Comment(id='f48kko0'), Comment(id='f4c8vbp'), Comment(id='f4car3h')]
    
    '''
    
    author_comments = filter_comments_from_authors(comments, authors_list)
    other_comments = []
    unwanted_comments = []
    filtered_list = []
    
    for comment in comments:
        if comment not in author_comments:
            other_comments.append(comment)
    
    for comment in other_comments:
        for reply in comment.replies:
            if reply.author in authors_list:
                unwanted_comments.append(reply)
                unwanted_comments.append(comment)
                
    for comment in other_comments:
        if comment not in unwanted_comments:
            filtered_list.append(comment)
    
    return filtered_list



def get_authors_from_topic(submission):
    '''(Submission) -> dict
    Returns dict where the keys are the authors of the comments in the submission
    and the value of the key is the number of comments the author has made in the submission
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/qo5qd4/cat_chasing_birds_outside_of_mcconnell_today_what/'
    >>> submission = reddit.submission(url=url)
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    20
    >>> num_comments_per_author['mb1167']
    3
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/moxbw2/cats/'
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    14
    >>> num_comments_per_author['sersaretheproduct']
    7
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/djtpmb/cat_on_campus/'
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    20
    >>> num_comments_per_author['nazaz']
    3
    
    '''
    
    comments_list = get_topic_comments(submission)
    authors_list = []
    number_of_comments_per_author = []
    dictionary = {}
    
    for comment in comments_list:
        if comment.author == None:     #Checks for deleted users, ID unavailable
            continue
        elif comment.author not in authors_list:
            authors_list.append(comment.author.name)   #comment.author is a redditor object, this allows
                                                        #to retrieve the username only
    
    for author in authors_list:
        count = 0
        for comment in comments_list:
            if comment.author == author:
                count +=1
        number_of_comments_per_author.append(count)
    
    
    for i in range(len(authors_list)):
        dictionary[authors_list[i]] = number_of_comments_per_author[i]
    
    
    return dictionary



def select_random_submission_url(reddit, topic_url, subreddit_name, replace_limit):
    '''(Reddit, str, str, int) -> Submission
    Function rolls a six-sided die
    If the die lands on 1 or 2, return Submission for the given topic_url after loading given
    number of extra comments
    Otherwise, return Submission corresponding to a random submission from the top submission of subreddit_name
    '''
    
    die_roll = random.randint(1, 6)
    more_comments = []
    
    if die_roll == 1 or die_roll == 2:
        submission = reddit.submission(url=topic_url)
        submission.comments.replace_more(limit=None) 
        return submission
    
    else:
        submission_list = []
        for submission in reddit.subreddit(subreddit_name).top('all'):
            submission_list.append(submission)
        
        submission = random.choice(submission_list)
        return submission




def post_reply(submission, username):
    '''(Submission, str) -> None
    Returns nothing
    If bot did not make any replies to submission, create a new top-level comment with text
    given by generate_comment()
    Otherwise, random comment from all comments in submission that the bot has not already replied to
    is chosen and the bot replies to it with text given by generate_comment()
    '''    
    
    my_dictionary = get_authors_from_topic(submission)
    comments = get_topic_comments(submission)
    
    if username not in my_dictionary:
        bot_reply = generate_comment()
        submission.reply(bot_reply)
    
    else:
        available_comments = filter_out_comments_replied_to_by_authors(comments, [username]) #possible comments the bot can reply to
        comment_option = random.choice(available_comments)
        bot_reply = generate_comment()
        comment_option.reply(bot_reply)


def bot_daemon(reddit, topic_url, replace_limit, subreddit_name, username):
    '''(Reddit, str, int, str, str) -> None
    Function calls select_random_submission_url function to get a Submission object,
    then calls post_reply function to reply to that submission
    and calls time.sleep(60) to make program sleep for 60 seconds before repeating the loop
    '''
    
    while True:
        submission = select_random_submission_url(reddit, topic_url, subreddit_name, replace_limit)
        post_reply(submission, username)
        time.sleep(60)
    
        
if __name__ == "__main__":
    
    reddit = praw.Reddit('bot', config_interpolation="basic")