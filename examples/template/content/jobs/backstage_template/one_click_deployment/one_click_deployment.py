cities = [
    "sydney", "melbourne", "brisbane", "perth", "adelaide", "goldcoast", "canberra", "newcastle", "wollongong", "logan",
    "geelong", "hobart", "townsville", "cairns", "toowoomba", "darwin", "launceston", "ballarat", "bendigo", "albury",
    "mackay", "rockhampton", "bunbury", "coffsharbour", "bundaberg", "herveybay", "mildura", "shepparton", "gladstone", "portmacquarie",
    "tamworth", "orange", "dubbo", "kalgoorlie", "bathurst", "warrnambool", "nowra", "wagga", "lismore", "alice",
    "mountgambier", "geraldton", "bowral", "armidale", "broome", "porthedland", "whyalla", "portaugusta", "devonport", "mountisa",
    "echuca", "emerald", "karratha", "portlincoln", "morwell", "griffith", "forster", "goulburn", "inverell", "parkes",
    "brokenhill", "swan", "gympie", "kingaroy", "roma", "warwick", "murraybridge", "naracoorte", "portpirie", "sale",
    "taree", "traralgon", "wangaratta", "warragul", "yeppoon", "bairnsdale", "batemansbay", "coffs", "dalby", "esperance",
    "goondiwindi", "horsham", "inverloch", "katherine", "lithgow", "maryborough", "moree", "murgon", "narrabri", "portfairy",
    "stanthorpe", "stawell", "ulladulla", "victorharbor", "yamba", "young", "zillmere", "emeraldqld", "emeraldvic"
]

template = """# Backstage Scaffolder Template for One-Click Deployment Workshop
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: rundeck-workshop-deployment-{city}
  title: 🚀 WORKSHOP One-Click Deployment ({citytitle})
  description: Learn why Rundeck rocks! Deploy with ONE button click, auto-rollback if things break, no terminal commands needed for {citytitle}.
  tags:
    - rundeck
    - workshop
    - deployment
    - kubernetes
    - {city}
spec:
  owner: user-{city}
  type: rundeck-orchestration
  parameters:
    - title: 🎓 Workshop Deployment Configuration
      required:
        - service_name
        - version
        - namespace
        - expected_code
        - max_retries
        - slack_channel
      properties:
        service_name:
          title: Service Name
          type: string
          description: Which service to deploy?
          default: demo-api
          enum:
            - demo-api
            - web-frontend
            - auth-service
            - payment-gateway
            - notification-service

        version:
          title: Version
          type: string
          description: Which version? (e.g., v1.2.3)
          default: v1.0.0
          pattern: '^v[0-9]+\\.[0-9]+\\.[0-9]+$'

        namespace:
          title: Kubernetes Namespace
          type: string
          description: Target namespace for deployment
          enum:
            - staging
            - dev
            - qa
          default: staging

        expected_code:
          title: Expected HTTP Code
          type: string
          description: Expected HTTP response code for health checks
          enum:
            - "200"
            - "201"
            - "204"
          default: "200"

        max_retries:
          title: Max Retries
          type: string
          description: Maximum number of health check retries
          enum:
            - "3"
            - "5"
            - "10"
          default: "3"

        slack_channel:
          title: Slack Channel
          type: string
          description: Slack channel for deployment notifications
          default: deployments-{city}

        waitForJob:
          title: Wait for completion
          type: boolean
          description: Wait for job to complete before finishing
          default: true

  steps:
    - id: rundeck-execute
      name: 🚀 Execute Workshop Deployment
      action: rundeck:job:execute
      input:
        jobId: workshop-{city}
        projectName: WORKSHOP_OPS
        parameters:
          service_name: ${{{{ parameters.service_name }}}}
          version: ${{{{ parameters.version }}}}
          namespace: ${{{{ parameters.namespace }}}}
          expected_code: ${{{{ parameters.expected_code }}}}
          max_retries: ${{{{ parameters.max_retries }}}}
          slack_channel: ${{{{ parameters.slack_channel }}}}
        waitForJob: ${{{{ parameters.waitForJob }}}}

  output:
    links:
      - title: 🎯 Rundeck Execution
        url: ${{{{ steps['rundeck-execute'].output.executionId }}}}
        icon: dashboard
      - title: 📊 Deployment Dashboard
        url: https://monitoring.company.com/deployments/{city}
        icon: monitoring
      - title: 🤖 Johnny 5 Status
        url: https://rundeck.company.com/project/WORKSHOP_OPS
        icon: catalog
    text:
      - title: 🎉 Deployment Summary
        content: |
          ✨ Workshop deployment initiated for {citytitle}!
          
          Service: ${{{{ parameters.service_name }}}}
          Version: ${{{{ parameters.version }}}}
          Namespace: ${{{{ parameters.namespace }}}}
          
          What's happening:
          ✅ Deploying to Kubernetes
          ✅ Running automated health checks
          ✅ Auto-rollback safety net active
          ✅ Zero manual commands needed!
      - title: 📝 Execution Logs
        content: ${{{{ steps['rundeck-execute'].output.logs }}}}
"""

# Generate the YAML files
for city in cities:
    with open(f"workshop-deployment-{city}.yaml", "w") as f:
        f.write(template.format(city=city, citytitle=city.title()))

print("✅ Generated Backstage YAML templates for all cities!")
print(f"📦 Total files created: {len(cities)}")
print("🎓 Workshop templates ready for deployment!")