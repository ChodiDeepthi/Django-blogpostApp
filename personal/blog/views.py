from django.shortcuts import render

# Create your views here.


from datetime import date
post_datas=[

    {
        "slug":"hike-in-the-mountains",
        "image":"images/image.png",
        "author":"deepthi",
        "date":date(2024,7,31),
        "title":"Mountain Hiking",
        "excert":"Mountain hiking is a thrilling way to explore nature’s heights, offering breathtaking views, challenging trails, and a sense of adventure. Whether trekking up rugged paths, navigating steep ascents, or traversing serene alpine landscapes, mountain hiking offers both physical and mental rewards. It requires a mix of endurance, balance, and careful planning, as well as respect for changing weather and altitude.",
        "content":"""Mountain hiking is more than just a physical activity—it’s an immersive journey into nature’s grandeur, with each trail revealing something unique. For those drawn to the allure of high-altitude adventures, mountain hiking offers a mix of thrilling challenges and deep rewards. In this blog, we’ll explore the essentials for a successful mountain hike, from preparation tips to finding the best trails, and share insights on why it’s an experience like no other. """

    },
    {
        "slug":"adventures",
        "image":"images/travel.jfif",
        "author":"deepthi",
        "date":date(2024,10,25),
        "title":"Travelling",
        "excert":"Traveling is not just about reaching a destination; it's about the journey itself. Each new place offers a tapestry of experiences, woven from the sights, sounds, and flavors of diverse cultures. As you step into unfamiliar streets, you breathe in the stories that linger in the air—the laughter of children playing, the aroma of street food sizzling in the pan, and the rhythm of life unfolding around you.",
        "content":""" Traveling is not just about reaching a destination; it's about the journey itself. Each new place offers a tapestry of experiences, woven from the sights, sounds, and flavors of diverse cultures. As you step into unfamiliar streets, you breathe in the stories that linger in the air—the laughter of children playing, the aroma of street food sizzling in the pan, and the rhythm of life unfolding around you.

Every travel experience is an opportunity for personal growth and discovery. Whether it's climbing a mountain, wandering through ancient ruins, or simply enjoying a quiet moment in a bustling café, each adventure expands your perspective. You meet people who challenge your beliefs and share stories that inspire you.

In the end, traveling transforms you. It enriches your soul, broadens your horizons, and creates lasting memories that you carry with you long after the journey ends. So pack your bags, embrace the unknown, and let the world unfold before you."""

    },
    {
        "slug":"walking-in-parks",
        "image":r"images\group.webp",
        "author":"deepthi",
        "date":date(2024,10,4),
        "title":"Waling in parks",
        "excert":"king in parks is a simple yet refreshing way to connect with nature and unwind from daily routines. Surrounded by greenery, gentle trails, and the sounds of birds and rustling leaves, a park walk offers a peaceful escape and a boost to both physical and mental well-being. Whether you're strolling along flower-lined paths, pausing by a lake, or just enjoying the open air, walking in parks is a rejuvenating activity suitable for all ages. It’s a perfect blend of relaxation and exercise, inviting us to slow down and enjoy the beauty around us.",
        "content":"""Walking in parks is one of life’s simplest pleasures—a chance to step away from the noise of daily routines and reconnect with nature. Unlike structured workouts or high-intensity activities, a stroll through a park offers a more relaxed, mindful experience that can benefit the body, mind, and soul. In this blog, we’ll explore the many reasons why walking in parks is a great habit to develop, how it can boost your health, and a few tips for making the most of your time outdoors.
Parks provide a refreshing, natural setting filled with trees, flowers, open spaces, and sometimes even lakes or streams. Walking through these serene environments allows us to slow down, breathe deeply, and take in the beauty around us. Unlike urban sidewalks or gym treadmills, parks offer varied landscapes that make each walk unique, creating a much-needed mental reset. """

    },
    {
        "slug":"Planting-works",
        "image":r"images\garden.jfif",
        "author":"deepthi",
        "date":date(2024,10,27),
        "title":"House plant work",
        "excert":"Houseplants bring vibrancy and fresh air into any space, but they also need regular care to stay healthy and beautiful. Two of the most important aspects of plant care are cleaning and watering, which not only support growth but also help prevent common issues like dust buildup and root rot. Here’s a quick guide to keeping your indoor plants in top shap",
        "content":"""Houseplants bring vibrancy and fresh air into any space, but they also need regular care to stay healthy and beautiful. Two of the most important aspects of plant care are cleaning and watering, which not only support growth but also help prevent common issues like dust buildup and root rot. Here’s a quick guide to keeping your indoor plants in top shap. Houseplants bring vibrancy and fresh air into any space, but they also need regular care to stay healthy and beautiful. Two of the most important aspects of plant care are cleaning and watering, which not only support growth but also help prevent common issues like dust buildup and root rot. Here’s a quick guide to keeping your indoor plants in top shap """

    }


]


#showing latest posts
def get_date(post):
    return post['date']
sorted_posts=sorted(post_datas,key=get_date)
latest_posts=sorted_posts[-3:]





def home_page(request):
    #return render(request,"blog/home.html")
    return render(request,"blog/home.html",{"posts":latest_posts})


def posts(request):
    return render(request,"blog/allposts.html",{"all_posts":post_datas})
def post_detail(request,slug):
    current=next(post for post in post_datas if post['slug']==slug)
    return render(request,"blog/post-detaile.html",{"post":current})
