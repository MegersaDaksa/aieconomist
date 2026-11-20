# AI economics review — November 19, 2026

**Information cutoff:** November 19, 2026, 10 PM ET. **Status:** Independently researched brief, prepared for the AI Economist repository. The scheduled *This Week in AI* editorial review had no recorded result at the time of preparation and is due November 20.

## Economic signal

Recent model releases, chip sales, cloud revenues, public equity issuance, and power projections illustrate the interconnected demand for AI services and the infrastructure supporting them. The economic question is whether accepted output and customer revenue grow enough to justify compute, capital, and energy commitments.

| Date | Verified development | Economic relevance and next question |
| --- | --- | --- |
| Nov 17 | OpenAI released GPT-6.2 Astra and Sol. Its published standard short-context API rates per million input/output tokens are $8/$40 for Astra and $2/$10 for Sol. | A fourfold difference in these rates creates a choice between models. Compare cost per accepted deliverable, rework, latency, and quality under identical task conditions. [Release index](https://openai.com/research/index/release/) and [pricing](https://developers.openai.com/api/docs/pricing). |
| Nov 17 | NVIDIA reported fiscal Q3 2027 revenue of $115.8B and data center revenue of $107.6B, up 110% year over year, for the quarter ending October 25. | Strong supplier sales show investment in compute infrastructure. Buyer utilization, depreciation, and revenue are needed to assess the return on this investment. [NVIDIA results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027). |
| Nov 18–19 | Anthropic priced its IPO at $83 per share. The final prospectus reports $81.34B total offering value and about $78.84B proceeds to the issuer after underwriting discounts and before other expenses. The NYSE market desk reported an opening trade at $111.50 on Nov 19 for Nasdaq-listed ANT. Settlement was expected Nov 20. | Distinguish capital raised from market capitalization and operating revenue. Track cash spending, compute commitments, revenue quality, and gross margins as disclosures become available. [SEC prospectus](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074944/anthropicpbc-424b4.htm), [issuer IR](https://investor.anthropic.com/overview/default.aspx), [NYSE market desk](https://e.nyse.com/mac-desk-midday-market-update). |
| Nov 19 | Alibaba reported September-quarter AI Cloud and Compute Services revenue of RMB 61B, up 53% year over year. External customers accounted for RMB 47B; internal customers for RMB 14B. | External recurring revenue, equipment solutions, and internal consumption carry different implications for monetization. Follow margins and capital requirements alongside growth. [Issuer quarterly release, AI Cloud and Compute Services table](https://data.alibabagroup.com/ecms-files/1532295521/e676aff4-e76d-489b-960a-47b9cf36485d/Alibaba%20Group%20Announces%20September%20Quarter%202026%20Results%20and%20Interim%20Results%20for%20the%20Six%20Months%20Ended%20September%2030%2C%202026.pdf). |
| Nov 19 | The IEA released World Energy Outlook 2026. Figure 1.38 in its Stated Policies Scenario shows approximately 550 TWh of global electricity generation for data centers in 2025 rising to approximately 1,150 TWh in 2030. | This is a scenario projection for all data centers. Test local power availability, interconnection costs, tariffs, and capacity delays before extrapolating it to individual AI investments. [IEA report](https://www.iea.org/reports/world-energy-outlook-2026) and [Figure 1.38, p. 84](https://www.iea.org/files/41082112-1153-4b16-b738-d44fb273dfd9/WorldEnergyOutlook2026.pdf). |

## Economics exercise — price per accepted output

Illustrative task with 10,000 uncached input tokens and 2,000 billable output tokens per attempt, standard short-context rates, no extra tools or caching. Astra costs $0.16 per attempt and Sol costs $0.04. With equal labor and overhead, a $0.12 per-attempt difference is the maximum extra expected cost that Sol can incur before the initial price advantage disappears. If Astra always succeeds and Sol has an independent probability of acceptance per attempt, with unlimited fully charged identical retries and zero review cost, Sol breaks even at 25% acceptance. Real use requires measuring review labor, task failures, latency and material errors; the assumptions are illustrative.

## Research priorities

| Question | Method | Evidence needed |
| --- | --- | --- |
| When do lower token prices translate to lower accepted-output costs? | Matched task benchmark against fixed quality rubric | Token category and usage logs, retries, review minutes, acceptance and material-error outcomes |
| When does compute demand justify capacity expansion? | Demand-by-workload model, utilization and delivery-risk scenarios, incremental NPV | Workload volumes, throughput, accelerator-hour costs, fixed commitments and utilization |
| How does public equity financing translate into productive AI capital? | Financing and investment bridge by issuer and disclosure period | Prospectuses, financial statements, compute commitment disclosures, cash flow and segment metrics |
| Who bears power infrastructure costs? | Site-level capacity, tariff, and incidence scenarios | Grid connection schedule, contracted MW, power prices, usage profile, facility efficiency and allocation rules |

## Next action

Extend the existing [AI workflow economics project](../../projects/ai-workflow-economics/README.md) with a controlled token-cost benchmark. Document one common task, model and pricing snapshots, fixed evaluation rubric, and repeatable test protocol. Then use measured task costs and volumes as inputs to an infrastructure investment scenario.

## Editorial draft

AI has become an economic supply chain. An AI request generates demand for compute, chips, cloud capacity, electricity and financing. Recent disclosures from AI companies and suppliers show activity at each layer. An economist must connect the revenue opportunity to utilization, capital costs, and accepted output quality. The central question is whether AI adoption produces enough value to cover the resources it consumes.

**Scope:** This is a selected research review, not a comprehensive news or IPO census. No market-close return or investment recommendation is asserted.
