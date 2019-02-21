#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import sys

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

if len(sys.argv) <= 1:
    raise ValueError('Credentials not passed as arguments')

print('Logging in with credentials: ')
print(f"Username: {sys.argv[1]}")
print(f"Password: {sys.argv[2]}")

bot = InstaBot(
    login=sys.argv[1],
    password=sys.argv[2],
    like_per_day=700,
    comments_per_day=100,
    tag_list=["streetart", "art", "graffiti", "photography", "streetphotography", "street", "urbanart", "photooftheday", "instagood", "artist", "love", "bnw", "photo", "travel", "streetstyle", "urban", "artwork", "life", "city", "ig", "mural", "painting", "graffitiart", "blackandwhite", "fashion", "photographer", "portrait", "architecture", "picoftheday", "beach", "sunset", "nature", "sun", "sea", "sky", "pretty", "follow", "dog", "beautiful", "blue", "fun", "summer", "clouds", "beauty", "bestoftheday", "cool", "f", "hair", "amazing", "swag", "djiglobal", "gopro", "goproarg", "beachlife", "wanderlust", "escapecampervans", "chasingsunsets", "wanderers", "worldexplorer", "design", "interiordesign", "architecturephotography", "building", "landscape", "archilovers", "architect", "instatravel", "like", "arquitectura", "luxury", "home", "interior"],
    tag_blacklist=["rain", "thunderstorm"],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=0,
    follow_time=10 * 60 * 60,
    unfollow_per_day=500,
    unlike_per_day=0,
    unfollow_recent_feed=True,  # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
    time_till_unlike=3 * 24 * 60 * 60,  # 3 days
    unfollow_break_min=15,
    unfollow_break_max=30,
    user_max_follow=9000,
    # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
    user_min_follow=100,
    log_mod=0,
    proxy="",
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[
        ["this", "the", "your"],
        ["photo", "picture", "pic", "shot"],
        ["is", "looks", "is 👉", "is really"],
        [
            "great",
            "super",
            "good",
            "very good",
            "wow",
            "WOW",
            "cool",
            "GREAT",
            "magnificent",
            "magical",
            "very cool",
            "stylish",
            "beautiful",
            "so beautiful",
            "so stylish",
            "so professional",
            "lovely",
            "so lovely",
            "very lovely",
            "glorious",
            "so glorious",
            "very glorious",
            "adorable",
            "excellent",
            "amazing",
        ],
        [".", "🙌", "... 👏", "!", "! 😍", "😎"]
    ],
    # Use unwanted_username_list to block usernames containing a string
    # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    # 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        "second",
        "stuff",
        "art",
        "project",
        "love",
        "life",
        "food",
        "blog",
        "free",
        "photo",
        "graphy",
        "indo",
        "travel",
        "art",
        "shop",
        "store",
        "sex",
        "toko",
        "jual",
        "online",
        "murah",
        "jam",
        "kaos",
        "case",
        "baju",
        "fashion",
        "corp",
        "tas",
        "butik",
        "grosir",
        "karpet",
        "sosis",
        "salon",
        "skin",
        "care",
        "cloth",
        "tech",
        "rental",
        "kamera",
        "beauty",
        "express",
        "kredit",
        "collection",
        "impor",
        "preloved",
        "follow",
        "follower",
        "gain",
        ".id",
        "_id",
        "bags",
    ],
    unfollow_whitelist=['j_pou_g', 'tomaspiaggio', 'pilispadaro', 'additionstudios'],
    # Enable the following to schedule the bot. Uses 24H
    end_at_h = 22, # Hour you want the bot to stop
    # end_at_m = 30, # Minute you want the bot stop, in this example 23:30
    start_at_h = 8, # Hour you want the bot to start
    # start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
)

bot.mainloop()
