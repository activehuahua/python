#!/usr/bin/python3
# -*-coding:utf-8 -*-

base_url = 'https://redmine.silksoftware.com/login?back_url=https%3A%2F%2Fredmine.silksoftware.com%2F'
login_url = 'https://redmine.silksoftware.com/login'
domain = 'https://redmine.silksoftware.com/'

uat_url = 'https://redmine.silksoftware.com/projects/hm-magento-qa/issues'
app_url = 'https://redmine.silksoftware.com/projects/hm-app/issues'

low_url = '?utf8=%E2%9C%93&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=1&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&c%5B%5D=due_date&c%5B%5D=fixed_version&c%5B%5D=cf_4&group_by='
normal_url = '?utf8=%E2%9C%93&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=2&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&c%5B%5D=due_date&c%5B%5D=fixed_version&c%5B%5D=cf_4&group_by='
high_url = '?utf8=%E2%9C%93&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&c%5B%5D=due_date&c%5B%5D=fixed_version&c%5B%5D=cf_4&group_by='
urgent_url = '?utf8=%E2%9C%93&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&c%5B%5D=due_date&c%5B%5D=fixed_version&c%5B%5D=cf_4&group_by='
immediate_url = '?utf8=✓&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&c%5B%5D=due_date&c%5B%5D=fixed_version&c%5B%5D=cf_4&group_by='

UATData = {
    'UAT Low:': uat_url + low_url,
    'UAT Normal:': uat_url + normal_url,
    'UAT High:': uat_url + high_url,
    'UAT Urgent:': uat_url + urgent_url,
    'UAT Immediate': uat_url + immediate_url
}

AppData = {
    'APP Low:': app_url + low_url,
    'APP Normal:': app_url + normal_url,
    'APP High:': app_url + high_url,
    'APP Urgent:': app_url + urgent_url,
    'APP Immediate': app_url + immediate_url
}