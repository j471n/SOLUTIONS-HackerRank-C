/*
For 
*/

SELECT RPAD('*', 2 * LEVEL - 1, ' *')
FROM DUAL CONNECT BY LEVEL <= 20;
