from client import AutonomousPriceNegotiationDiscountBrokerClient

def main():
    client = AutonomousPriceNegotiationDiscountBrokerClient()
    res = client.negotiate_order_concession(850.00, 3200.00, 'MEDIUM')
    print('Price Negotiation Broker: ' + res['negotiation_session_id'])
    print('Original: $' + str(res['original_price_usd']) + ' -> Final: $' + str(res['final_negotiated_price_usd']) + ' (-' + str(res['concession_discount_pct']) + '%)')
    print('Coupon Code: ' + res['authorized_coupon_code'] + ' | Margin Protected: ' + str(res['merchant_margin_floor_protected']))
    print('Contract Token: ' + res['concession_contract_token_url'])

if __name__ == '__main__':
    main()
