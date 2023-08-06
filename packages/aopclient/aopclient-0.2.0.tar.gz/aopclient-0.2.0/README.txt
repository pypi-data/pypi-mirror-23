# aopclient
Client for the AOP

Sample code:


from aopclient import AOLClient
client = AOLClient()
client.show_config()
client.connect()
client.get_organizations()
client.get_campaigns(org_id)
client.get_campaigns_by_advertiser(org_id, ad_id)
client.get_campaigns_by_advertiser_by_campaign(org_id, ad_id, campaign_id)
tactics = client.get_tactics_by_campaign(org_id, ad_id, campaign_id)
creatives = client.get_creative_assignments(org_id, ad_id, campaign_id, tactic_id)
private_deal_assignments = client.get_deal_assignments(org_id, ad_id, campaign_id, tactic_id)
