from collections import Counter


def get_count_visits_from_ip(ips):
    return dict(Counter(ips))



def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]


# ip = [
#     "85.157.172.253",
#     "85.157.172.255",
#     "85.157.172.110",
#     "85.157.172.253",
#     "85.157.172.211",
#     "85.157.172.210",
#     "85.157.172.255",
#     "85.157.172.207",
#     "85.157.172.253"
# ]
# get_count = get_count_visits_from_ip(ip)
# print(get_count)
# print(get_frequent_visit_from_ip(get_count))
