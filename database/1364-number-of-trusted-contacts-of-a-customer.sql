SELECT
  Invoices.invoice_id,
  Customers.customer_name,
  Invoices.price,
  COUNT(Co.user_id) AS contacts_cnt,
  COUNT(Cu.email) AS trusted_contacts_cnt
FROM Invoices
INNER JOIN Customers ON (Invoices.user_id = Customers.customer_id)
LEFT JOIN Contacts AS Co ON (Customers.customer_id = Co.user_id)
LEFT JOIN Customers AS Cu ON (Co.contact_email = Cu.email)
GROUP BY 1
ORDER BY 1;
