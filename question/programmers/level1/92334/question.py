# id_list = ['muzi', 'frodo', 'apeach', 'neo']
# report = ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi']
# k = 2

id_list = ['con', 'ryan']
report = ['ryan con', 'ryan con', 'ryan con', 'ryan con']
k = 3


def solution(id_list, report, k):
    report_list = list(set(report))

    reported_list = [0] * len(id_list)
    my_report_list = [[] for _ in range(len(id_list))]

    for i in range(len(id_list)):
        for j in range(len(report_list)):
            reporter, reported = report_list[j].split()
            if id_list[i] == reported:
                reported_list[i] += 1
            if id_list[i] == reporter:
                my_report_list[i].append(reported)

    answer = [0] * len(id_list)

    for i in range(len(id_list)):
        if reported_list[i] >= k:
            for j in range(len(id_list)):
                if id_list[i] in my_report_list[j]:
                    answer[j] += 1

    return answer


print(solution(id_list, report, k))
