WITH plan_changes AS (
  SELECT
    spender_id,
    plan,
    card_activation_date AS start_date,
    LEAD(card_activation_date) OVER (PARTITION BY spender_id ORDER BY card_activation_date) AS end_date
  FROM `data_analyst_case.card_transactions`
),

winning_transactions AS (
  SELECT
    operation_id,
    date AS transaction_date,
    amount,
    member_id AS user_id
  FROM `data_analyst_case.roulette_winners`
)

, winners_properties as (SELECT
  wt.operation_id,
  wt.transaction_date,
  wt.amount,
  wt.user_id,
  pc.plan
FROM winning_transactions wt
LEFT JOIN plan_changes pc
ON
  wt.user_id = pc.spender_id
  AND wt.transaction_date >= pc.start_date
  AND (wt.transaction_date < pc.end_date OR pc.end_date IS NULL))


SELECT

      transaction_date as date_reimbursement,
      round(SUM(case when plan = 'lydia_black' then amount*2 else amount end), 2) as amount_paid,
      count(distinct operation_id) as count_transaction,
      round(SUM(case when plan = 'lydia_black' then 1 else 0 end)/SUM(1)*100, 2) as black_plan_prop,
      round(SUM(case when plan = 'lydia_blue' then 1 else 0 end)/SUM(1)*100, 2) as blue_plan_prop,
      round(SUM(case when plan = 'no_plan' then 1 else 0 end)/SUM(1)*100, 2) as noplan_prop,


      FROM winners_properties
      GROUP BY 1
      ORDER BY 1 DESC