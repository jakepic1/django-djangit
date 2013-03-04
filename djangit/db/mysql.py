import generic

class Engine(generic.Engine):
    copy_command = ' '.join((
        'mysqladmin -u{USER} -h {HOST} --password=\'{PASSWORD}\' CREATE {BRANCH_DB};',
        'mysqldump -u{USER} -h {HOST} --password=\'{PASSWORD}\' {NAME}',
        '| mysql -u{USER} -h {HOST} --password=\'{PASSWORD}\' {BRANCH_DB}',
    ))
    drop_command = (
        'mysqladmin -f -u{USER} -h {HOST} --password=\'{PASSWORD}\' DROP {BRANCH_DB}'
    )
