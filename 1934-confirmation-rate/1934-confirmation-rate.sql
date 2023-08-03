# Write your MySQL query statement below
select s.user_id,round(avg(
case 
when c.action='confirmed' then 1.00 
else 0.00
end),2) as confirmation_rate
from signups s left join confirmations c 
on s.user_id=c.user_id
group by s.user_id







