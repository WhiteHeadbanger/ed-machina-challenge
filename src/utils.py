

def get_response_from_query(query):
    career_list = []
    result = {}
    result["careers"] = []
    index = 0
    for q in query:
        result["name"] = q[0]
        result["email"] = q[1]
        result["address"] = q[2]
        result["phone"] = q[3]
        result["inscription_year"] = q[4]

        if q[5] not in career_list:
            index += 1
            career_list.append(q[5])
            result["careers"].append({"name":q[5], "courses":[]})

        career = result["careers"][index-1]
        career["courses"].append({"name":q[6], "course_time":q[7], "course_times_quantity":q[8]})
    
    return result