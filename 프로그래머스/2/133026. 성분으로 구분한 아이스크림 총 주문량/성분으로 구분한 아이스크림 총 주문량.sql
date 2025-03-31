-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(H.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF AS H
    JOIN ICECREAM_INFO AS I ON H.FLAVOR = I.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER