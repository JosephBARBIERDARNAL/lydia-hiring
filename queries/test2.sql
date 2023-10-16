select plan,
count(*)
from `data_analyst_case.card_transactions`
group by 1