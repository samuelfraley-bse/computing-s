def has_experience_as(cvs, job_title):
    result = []
    for cv in cvs:
        if job_title in cv['jobs']:
            result.append(cv['user'])
    return result

def job_counts(cvs):
    counts = {}
    for cv in cvs:
        for job in cv['jobs']:
            if job not in counts:
                counts[job] = 0
            counts[job] += 1
    return counts

def most_popular_job(cvs):
    counts = job_counts(cvs)
    most = None
    num = 0
    for job, n in counts.items():
        if n > num:
            num = n
            most = job
    return (most, num)
