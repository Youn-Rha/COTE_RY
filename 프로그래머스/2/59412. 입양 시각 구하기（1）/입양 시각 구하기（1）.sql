-- 코드를 입력하세요
SELECT hour(datetime) as hour, count(*) from animal_outs
where hour(datetime) > 8 and hour(datetime) < 20
group by hour
order by hour