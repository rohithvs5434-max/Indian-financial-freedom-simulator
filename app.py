import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Indian Financial Freedom Simulator", page_icon="🇮🇳", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.block-container{max-width:1200px;padding-top:2rem;padding-bottom:3rem}
.hero{background:linear-gradient(135deg,#172554,#0f172a);border:1px solid #1e3a8a;border-radius:18px;padding:1.6rem 1.8rem;margin-bottom:1.4rem}
.hero h1{color:#eff6ff!important;margin:0 0 .4rem;font-size:2.25rem}.hero p{color:#cbd5e1!important;margin:0;line-height:1.6}
.step{background:#111827;border:1px solid #334155;border-radius:14px;padding:1rem;height:100%}.step b{color:#60a5fa}.step h4{color:#f8fafc!important;margin:.2rem 0}.step p{color:#94a3b8!important;font-size:.85rem}
.card{background:#111827;border:1px solid #334155;border-radius:14px;padding:1rem;min-height:135px}.label{color:#94a3b8!important;font-size:.85rem}.value{color:#f8fafc!important;font-size:1.6rem;font-weight:800;margin:.3rem 0}.help{color:#cbd5e1!important;font-size:.78rem;line-height:1.45}
.explain{background:#0f172a;border:1px solid #334155;border-left:4px solid #60a5fa;border-radius:12px;padding:1rem;margin:.7rem 0}.explain b{color:#93c5fd}.explain span{color:#cbd5e1;line-height:1.55}
.good{background:#052e16;border:1px solid #166534;border-radius:12px;padding:1.1rem;color:#dcfce7}.warn{background:#451a03;border:1px solid #92400e;border-radius:12px;padding:1.1rem;color:#fef3c7}.risk{background:#450a0a;border:1px solid #991b1b;border-radius:12px;padding:1.1rem;color:#fee2e2}
</style>
""", unsafe_allow_html=True)

def money(x):
    x=float(x)
    if x>=1e7:return f"₹{x/1e7:.2f} Cr"
    if x>=1e5:return f"₹{x/1e5:.2f} L"
    return f"₹{x:,.0f}"

def card(label,value,help_text):
    st.markdown(f'<div class="card"><div class="label">{label}</div><div class="value">{value}</div><div class="help">{help_text}</div></div>',unsafe_allow_html=True)

def explain(title,text):
    st.markdown(f'<div class="explain"><b>{title}</b><br><span>{text}</span></div>',unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def simulate(n,current_age,retirement_age,life,mutual,annual_save,epf,epf_month,epf_rate,ppf,ppf_annual,ppf_rate,nps,nps_month,nps_rate,ret_expense,equity,inflation,inflation_vol,scenario,seed):
    rng=np.random.default_rng(seed)
    total=life-current_age
    work=retirement_age-current_age
    ages=np.arange(current_age,life+1)
    stock_mean,stock_sd=.12,.15
    debt_mean,debt_sd=.07,.03
    inf=inflation
    if scenario=="High Inflation Stress": inf+=.02; stock_mean-=.02; debt_mean-=.01
    elif scenario=="Equity Bear Market Stress": stock_mean-=.04; debt_mean-=.005
    debt=1-equity
    port_return=equity*stock_mean+debt*debt_mean
    port_sd=equity*stock_sd+debt*debt_sd
    returns=rng.normal(port_return,port_sd,(total,n))
    infl=rng.normal(inf,inflation_vol,(total,n)); infl=np.clip(infl,-.02,.20)
    wealth=np.zeros((total+1,n)); expenses=np.zeros((total+1,n))
    mf=np.full(n,float(mutual)); ep=np.full(n,float(epf)); pp=np.full(n,float(ppf)); ns=np.full(n,float(nps))
    expenses[0]=ret_expense; wealth[0]=mf+ep+pp+ns
    for y in range(total):
        age=current_age+y+1; expenses[y+1]=expenses[y]*(1+infl[y]); r=returns[y]
        if age<=retirement_age:
            ep=(ep+epf_month*12)*(1+epf_rate/100)
            pp=(pp+ppf_annual)*(1+ppf_rate/100)
            nr=np.clip(nps_rate/100+(r-port_return)*.5,-.99,None)
            ns=(ns+nps_month*12)*(1+nr)
            mf=np.maximum((mf+annual_save)*(1+r),0)
            wealth[y+1]=mf+ep+pp+ns
        else:
            if age==retirement_age+1:
                mf=mf+ep+pp+ns; ep.fill(0); pp.fill(0); ns.fill(0)
            mf=np.maximum(mf-expenses[y+1],0); mf=np.maximum(mf*(1+r),0); wealth[y+1]=mf
    p10=np.percentile(wealth,10,axis=1); p50=np.percentile(wealth,50,axis=1); p90=np.percentile(wealth,90,axis=1)
    success=float(np.mean(wealth[-1]>0)*100)
    depletion=[]
    for i in range(n):
        z=np.where(wealth[work+1:,i]<=0)[0]
        if len(z): depletion.append(retirement_age+1+int(z[0]))
    return dict(ages=ages,wealth=wealth,expenses=expenses,p10=p10,p50=p50,p90=p90,success=success,ret_corpus=float(p50[work]),depletion=(float(np.median(depletion)) if depletion else None),port_return=port_return,port_sd=port_sd,work=work)

st.markdown('<div class="hero"><h1>🇮🇳 Indian Financial Freedom Simulator</h1><p>Enter your information from top to bottom. We explain what each number means, then calculate a retirement scenario for you.</p></div>',unsafe_allow_html=True)

st.markdown("### 🧭 How to use this simulator")
cols=st.columns(4)
for c,num,title,text in zip(cols,["STEP 1","STEP 2","STEP 3","STEP 4"],["Your Life","Your Money","Your Schemes","Your Answer"],["Age and retirement plan","Savings and spending","EPF, PPF and NPS","One button gives your analysis"]):
    with c: st.markdown(f'<div class="step"><b>{num}</b><h4>{title}</h4><p>{text}</p></div>',unsafe_allow_html=True)

with st.form("financial_profile_form"):
    st.markdown("## 📝 Step 1 — Your life")
    st.caption("These numbers tell the simulator how many years you have to build your corpus and how long it may need to last.")
    a,b,c=st.columns(3)
    with a:
        current_age=st.number_input("👤 Current age",18,100,33,1,help="Your age today.")
        st.caption("Example: 33")
    with b:
        retirement_age=st.number_input("🏖️ Planned retirement age",19,100,57,1,help="The age when you want employment income to stop.")
        st.caption("Example: 57")
    with c:
        life=st.number_input("❤️ Plan until age",20,110,86,1,help="The age until which you want the model to test your money.")
        st.caption("Example: 86")

    st.markdown("---")
    st.markdown("## 💰 Step 2 — Your money")
    st.caption("Enter the money already invested, how much you plan to add, and what you expect to spend in retirement.")
    a,b=st.columns(2)
    with a:
        mutual=st.number_input("📈 Current investments / mutual funds (₹)",0,100000000,1100000,50000,help="Current value of liquid investments included in this plan.")
        st.caption("₹11 lakh → enter 1100000")
        annual_save=st.number_input("💵 New investment each year (₹)",0,10000000,220000,10000,help="Expected yearly contribution to investments.")
        st.caption("₹20,000/month → ₹2,40,000/year")
    with b:
        ret_expense=st.number_input("🏠 Retirement spending per year, in today's money (₹)",120000,50000000,850000,25000,help="Your desired annual lifestyle cost expressed in today's purchasing power.")
        st.caption("₹50,000/month → ₹6,00,000/year")
        equity_pct=st.slider("📊 Equity allocation",0,100,70,5,help="Approximate share of liquid investments in equity/stocks.")
        st.caption(f"The remaining {100-equity_pct}% is modeled as debt/cash.")

    st.markdown("---")
    st.markdown("## 🏛️ Step 3 — Your EPF, PPF and NPS")
    st.caption("Don't have a scheme? Enter ₹0. These sections are grouped so you don't have to search for related fields.")
    a,b,c=st.columns(3)
    with a:
        st.markdown("### 🟢 EPF")
        epf=st.number_input("Current EPF balance (₹)",0,100000000,550000,50000,help="Current EPF corpus.")
        epf_month=st.number_input("EPF contribution per month (₹)",0,1000000,15000,1000,help="Monthly amount added to EPF.")
        epf_rate=st.number_input("EPF interest assumption (%)",0.0,15.0,8.25,.05)
    with b:
        st.markdown("### 🔵 PPF")
        ppf=st.number_input("Current PPF balance (₹)",0,100000000,220000,20000,help="Current PPF corpus.")
        ppf_annual=st.number_input("PPF contribution per year (₹)",0,200000,150000,10000,help="Expected annual PPF contribution.")
        ppf_rate=st.number_input("PPF interest assumption (%)",0.0,15.0,7.10,.05)
    with c:
        st.markdown("### 🟣 NPS")
        nps=st.number_input("Current NPS balance (₹)",0,100000000,320000,20000,help="Current NPS corpus.")
        nps_month=st.number_input("NPS contribution per month (₹)",0,1000000,12000,1000,help="Expected monthly NPS contribution.")
        nps_rate=st.number_input("NPS return assumption (%)",0.0,20.0,10.0,.10)

    st.markdown("---")
    st.markdown("## ⚙️ Step 4 — Simulation settings")
    st.caption("If you're not sure, leave these at the defaults. They are advanced assumptions, not required financial knowledge.")
    a,b,c=st.columns(3)
    with a: inflation=st.slider("🌡️ Expected inflation (%)",1.0,12.0,4.45,.05,help="Long-term inflation assumption.")
    with b: inflation_vol=st.slider("🌪️ Inflation uncertainty (%)",0.0,5.0,1.20,.10,help="How much annual inflation can vary.")
    with c: n=st.selectbox("🎲 Simulation scenarios",[500,1000,2000,5000],index=1,help="Number of possible future paths.")
    scenario=st.selectbox("🧪 Optional stress test",["None (Standard Baseline)","High Inflation Stress","Equity Bear Market Stress"],help="Use a stress test to see how the plan behaves in a difficult environment.")
    seed=st.number_input("Reproducible simulation seed",1,999999,42,1,help="Leave at 42 if you want repeatable results.")

    st.markdown("### ✅ Ready?")
    st.caption("Review the numbers above, then press the button. Results will appear immediately below.")
    submitted=st.form_submit_button("🚀 Calculate My Financial Freedom Plan",type="primary",use_container_width=True)

if submitted:
    if retirement_age<=current_age: st.error("Retirement age must be greater than current age."); st.stop()
    if life<=retirement_age: st.error("Life expectancy must be greater than retirement age."); st.stop()
    with st.spinner("🎲 Running your scenarios..."):
        result=simulate(int(n),int(current_age),int(retirement_age),int(life),float(mutual),float(annual_save),float(epf),float(epf_month),float(epf_rate),float(ppf),float(ppf_annual),float(ppf_rate),float(nps),float(nps_month),float(nps_rate),float(ret_expense),equity_pct/100,inflation/100,inflation_vol/100,scenario,int(seed))
    st.session_state.result=result
    st.session_state.profile=dict(current_age=current_age,retirement_age=retirement_age,life=life,mutual=mutual,annual_save=annual_save,ret_expense=ret_expense,equity_pct=equity_pct,epf=epf,epf_month=epf_month,ppf=ppf,ppf_annual=ppf_annual,nps=nps,nps_month=nps_month,inflation=inflation,scenario=scenario,n=n)

if "result" in st.session_state:
    r=st.session_state.result; p=st.session_state.profile
    st.markdown("---")
    st.markdown("## 🎯 Your Financial Freedom Results")
    st.caption("Read the first four cards first. They give you the simplest interpretation of the simulation.")
    a,b,c,d=st.columns(4)
    with a: card("Chance your money lasts",f"{r['success']:.1f}%","Share of simulated paths with money remaining at your selected life expectancy.")
    with b: card(f"Typical corpus at age {p['retirement_age']}",money(r['ret_corpus']),"The median modeled wealth when you reach retirement.")
    with c: card("Typical depletion point","Not reached" if r['depletion'] is None else f"Age {r['depletion']:.0f}","Median depletion age among paths that run out of money.")
    with d: card("Years until retirement",f"{r['work']} years",f"From age {p['current_age']} to age {p['retirement_age']}.")

    if r['success']>=85:
        st.markdown(f'<div class="good"><b>🟢 Strong modeled result</b><br><br>Your simulated success rate is <b>{r["success"]:.1f}%</b>. Most modeled paths remain funded to age {p["life"]}. This is not a guarantee.</div>',unsafe_allow_html=True)
    elif r['success']>=60:
        st.markdown(f'<div class="warn"><b>🟠 Review your plan</b><br><br>Your simulated success rate is <b>{r["success"]:.1f}%</b>. Try higher savings, lower retirement spending, a later retirement age, or a stress test.</div>',unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="risk"><b>🔴 High modeled risk</b><br><br>Your simulated success rate is <b>{r["success"]:.1f}%</b>. Many simulated paths run out before age {p["life"]}. Consider changing the plan assumptions.</div>',unsafe_allow_html=True)

    with st.expander("🔎 See exactly what you entered"):
        df=pd.DataFrame({"Input":["Current age","Retirement age","Plan until age","Current investments","Annual investment","Retirement spending","Equity allocation","EPF balance","PPF balance","NPS balance","Expected inflation","Stress test","Scenarios"],"Your value":[f"{p['current_age']} years",f"{p['retirement_age']} years",f"{p['life']} years",money(p['mutual']),money(p['annual_save']),money(p['ret_expense']),f"{p['equity_pct']}%",money(p['epf']),money(p['ppf']),money(p['nps']),f"{p['inflation']:.2f}%",p['scenario'],f"{p['n']:,}"]})
        st.dataframe(df,use_container_width=True,hide_index=True)

    st.markdown("### 📈 How your money could behave")
    st.caption("Green = better outcome, blue = typical outcome, red = difficult outcome. These are simulated scenarios, not predictions.")
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=r['ages'],y=r['p90'],name='Better outcome',line=dict(color='#10B981',dash='dash',width=2)))
    fig.add_trace(go.Scatter(x=r['ages'],y=r['p50'],name='Typical outcome',line=dict(color='#60A5FA',width=4)))
    fig.add_trace(go.Scatter(x=r['ages'],y=r['p10'],name='Difficult outcome',line=dict(color='#EF4444',dash='dot',width=2)))
    fig.add_vline(x=p['retirement_age'],line_dash='dash',line_color='#94A3B8',annotation_text='Retirement')
    fig.update_layout(template='plotly_dark',height=520,xaxis_title='Age',yaxis_title='Projected wealth (₹)',hovermode='x unified')
    st.plotly_chart(fig,use_container_width=True)

    st.markdown("### 💸 How retirement spending may rise with inflation")
    expenses=np.median(r['expenses'],axis=1)
    fig2=go.Figure(go.Scatter(x=r['ages'],y=expenses,name='Typical annual spending',line=dict(color='#F59E0B',width=3)))
    fig2.add_vline(x=p['retirement_age'],line_dash='dash',line_color='#94A3B8',annotation_text='Retirement')
    fig2.update_layout(template='plotly_dark',height=400,xaxis_title='Age',yaxis_title='Annual spending (₹)',hovermode='x unified')
    st.plotly_chart(fig2,use_container_width=True)

    st.markdown("### 🧠 What should you do next?")
    a,b,c=st.columns(3)
    with a: explain("💵 Save more", "Increase your annual investment and run the simulator again to see how much the success rate changes.")
    with b: explain("🏖️ Retire later", "Move your retirement age forward to give your investments more years to compound and fewer years to fund withdrawals.")
    with c: explain("🏠 Spend less", "Reduce annual retirement spending to reduce the withdrawal pressure on your portfolio.")

    with st.expander("📚 Understand the calculation"):
        explain("Accumulation", "Before retirement, the model adds your annual investment, EPF/PPF/NPS contributions and modeled returns.")
        explain("Monte Carlo", "The model generates many possible return and inflation paths and summarizes them using 10th, 50th and 90th percentile wealth paths.")
        explain("Retirement", "At retirement, the modeled EPF, PPF and NPS balances are combined with the liquid portfolio, and retirement spending is withdrawn each year.")
        explain("Success rate", "A path is successful when the simulated portfolio remains above zero at the end of the selected life-expectancy horizon.")

    st.caption("⚠️ Educational simulation only. It is not financial, investment, tax, pension or retirement advice. Actual returns, inflation, taxes, fees, scheme rules and personal circumstances may differ substantially.")
