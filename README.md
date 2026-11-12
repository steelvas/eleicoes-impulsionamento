# Eleições: uma empresa pode pagar para ampliar uma postagem?

Uma empresa oferece pagar pelo impulsionamento de um anúncio eleitoral favorável a uma candidatura.

```python
contratante = "empresa_privada"

autorizados = {
    "candidato", "partido", "federacao",
    "coligacao", "administrador_financeiro"
}

if contratante not in autorizados:
    print("BLOQUEAR a contratação")
else:
    print("Conferir conteúdo, identificação, plataforma e período")
```

1. **Código:** pagar pelo anúncio é um ato diferente de publicar uma opinião.
2. **Resultado:** não basta o conteúdo favorecer uma candidatura; é preciso verificar quem contratou o alcance.
3. **Regra:** o impulsionamento eleitoral é uma exceção à vedação de propaganda paga na internet. Deve ser identificado e contratado pelos agentes autorizados, diretamente com o provedor, para promover candidatura ou agremiação — não para propaganda negativa.
4. **O que fazer:** guardar identificação do contratante, peça publicada, comprovante, período e configuração do anúncio. A circulação paga ou impulsionada deve ser desligada desde 48 horas antes até 24 horas depois da eleição, mesmo se contratada anteriormente.

**Papel do advogado:** conferir a operação real da plataforma e da equipe de mídia; uma cláusula contratual não desliga um anúncio que continua circulando.

Fonte: [Resolução TSE nº 23.610/2019, art. 29, com alterações posteriores](https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-610-de-18-de-dezembro-de-2019).

*Exemplo didático. O código não libera automaticamente nenhum anúncio.*
