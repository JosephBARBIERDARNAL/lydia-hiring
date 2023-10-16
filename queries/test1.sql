SELECT COUNT(DISTINCT rw.member_id) AS nombre_commun
FROM `data_analyst_case.roulette_winners` rw
JOIN `data_analyst_case.card_transactions` ct ON rw.member_id=ct.spender_id