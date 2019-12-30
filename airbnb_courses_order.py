'''
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. 
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
'''

def find_courses_order(courses):
    ans = []
    # preprocess for listing all courses 
    # and make a dict for { pre-crs -> set of next courses}
    # for making a graph in completing the courses.
    next_crs = set()
    other_crs = set()
    pre_req_dict = {}
    for crs in courses:
        if courses[crs]:
            other_crs.add(crs)
            for crs_pre in courses[crs]:
                if crs_pre not in pre_req_dict:
                    pre_req_dict[crs_pre] = set()
                pre_req_dict[crs_pre].add(crs)
        else:
            next_crs.add(crs)
    
    no_of_turn = 0
    while next_crs and no_of_turn<len(next_crs):
        crs = next_crs.pop()
        if crs not in other_crs:
            ans.append(crs)
            if crs in pre_req_dict:
                items = pre_req_dict[crs]
                del pre_req_dict[crs]
                for course in items:
                    next_crs.add(course)
                other_crs.clear()
                for item in pre_req_dict:
                    other_crs.update(pre_req_dict[item])
            no_of_turn = 0
        else:
            next_crs.add(crs)
            no_of_turn += 1

    if next_crs:
        return None

    return ans


if __name__ == "__main__":
    data = [
            [
             {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
             ['CSC100', 'CSC200', 'CSCS300']
            ]
    ]
    for d in data:
        print('input', d[0], 'output', find_courses_order(d[0]))