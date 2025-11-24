cities = [
    "sydney", "melbourne", "brisbane", "perth", "adelaide", "goldcoast", "canberra", "newcastle", "wollongong", "logan",
    "geelong", "hobart", "townsville", "cairns", "toowoomba", "darwin", "launceston", "ballarat", "bendigo", "albury",
    "mackay", "rockhampton", "bunbury", "coffsharbour", "bundaberg", "herveybay", "mildura", "shepparton", "gladstone", "portmacquarie",
    "tamworth", "orange", "dubbo", "kalgoorlie", "bathurst", "warrnambool", "nowra", "wagga", "lismore", "alice",
    "mountgambier", "geraldton", "bowral", "armidale", "broome", "porthedland", "whyalla", "portaugusta", "devonport", "mountisa",
    "echuca", "emerald", "karratha", "portlincoln", "morwell", "griffith", "forster", "goulburn", "inverell", "parkes",
    "brokenhill", "swan", "gympie", "kingaroy", "roma", "warwick", "murraybridge", "naracoorte", "portpirie", "sale",
    "taree", "traralgon", "wangaratta", "warragul", "yeppoon", "bairnsdale", "batemansbay", "coffs", "dalby", "esperance",
    "goondiwindi", "horsham", "inverloch", "katherine", "lithgow", "maryborough", "moree", "murgon", "narrabri", "portfairy",
    "stanthorpe", "stawell", "ulladulla", "victorharbor", "yamba", "young", "zillmere", "emeraldqld", "emeraldvic"
]

with open("Deploy_AWS_Resources.yaml", "r") as f:
    job_template = f.read()

for city in cities:
    new_job = job_template.replace(
        "7fd537c4-4077-4404-a0ad-65cf19034b02",
        f"aws-provisioning-user-{city}"
    )
    with open(f"aws-job-user-{city}.yaml", "w") as out:
        out.write(new_job)