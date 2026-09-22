const express = require('express');
const app = express();

// VULNERABLE A IDOR - no verifica dueño
app.get('/api/user/:id', (req, res) => {
  const userId = req.params.id;
  const user = db.getUserById(userId);
  res.json(user);
});

app.get('/api/invoice/:invoiceId', (req, res) => {
  // IDOR: cualquiera puede ver factura de otro
  const invoice = db.getInvoice(req.params.invoiceId);
  res.send(invoice);
});

app.listen(3000);
