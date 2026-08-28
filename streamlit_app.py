# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under Apache-2.0.
from __future__ import annotations
import io, json, math
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import streamlit as st
from hadia.data import load_all, metadata, to_csv_bytes, to_json_bytes, tables_zip_bytes
from hadia.search import filter_df
from hadia.validate import validate_all

st.set_page_config(page_title="HADIA — Jharkhand's Digital Handia Knowledge Home",page_icon="🌾",layout="wide",initial_sidebar_state="expanded")

PALASH="#C94F18"; SAL="#315B3A"; EARTH="#744B2A"; RICE="#FFF9ED"; LAC="#8F2D2D"; GOLD="#D89B2B"
st.markdown(f"""<style>
.stApp {{ background: radial-gradient(circle at 80% 0%, #F6E7BF 0%, {RICE} 35%, #FFFDF7 100%); color:#24372B; }}
[data-testid="stSidebar"] {{ background: linear-gradient(180deg,#24372B 0%,#315B3A 55%,#704126 100%); }}
[data-testid="stSidebar"] * {{ color:#FFF9ED !important; }}
.hadia-hero {{padding:2.1rem 2.3rem;border-radius:26px;background:linear-gradient(135deg,#24372B 0%,#315B3A 58%,#744B2A 100%);box-shadow:0 18px 45px rgba(58,45,31,.18);margin-bottom:1.2rem;position:relative;overflow:hidden}}
.hadia-hero:after {{content:'✺'; position:absolute; right:28px; top:6px; font-size:118px; color:rgba(255,190,69,.12);}}
.hadia-hero h1 {{color:#FFF7E3;margin:0;font-size:3rem;letter-spacing:.02em}} .hadia-hero p {{color:#F3DFC0;font-size:1.08rem;max-width:850px}}
.tag {{display:inline-block;background:#C94F18;color:white;padding:.32rem .68rem;border-radius:999px;font-weight:700;font-size:.78rem;margin-right:.35rem}}
.card {{background:rgba(255,255,255,.82);border:1px solid #ead8b7;border-radius:18px;padding:1rem 1.1rem;box-shadow:0 7px 20px rgba(75,55,25,.06);height:100%}}
.card h3 {{color:#315B3A;margin-top:0}} .small {{color:#6B6259;font-size:.9rem}}
.passport {{border-left:7px solid {PALASH};background:#fff;border-radius:16px;padding:1rem 1.2rem;box-shadow:0 5px 18px rgba(70,50,25,.08)}}
.foot {{text-align:center;color:#75695c;font-size:.82rem;padding:2rem 0 .4rem}}
div[data-testid="stMetric"] {{background:rgba(255,255,255,.75);border:1px solid #ead8b7;padding:10px 14px;border-radius:16px}}
</style>""",unsafe_allow_html=True)

@st.cache_data
def all_data(): return load_all()
D=all_data(); META=metadata()

with st.sidebar:
    st.markdown("## 🌾 HADIA")
    st.caption("Digital Knowledge Home of Jharkhand's Handia")
    page=st.radio("Explore",["Home","Evidence Explorer","Jharkhand Atlas","Ranu & Plants","Microbes & Chemistry","Culture & Policy","Evidence Passport","Knowledge Graph","Research Gaps","Sources","Download Data","About & Methods"],label_visibility="collapsed")
    st.markdown("---")
    st.caption(f"HADIA-KB v{META['version']} · {META['release_date']}")
    st.caption("Evidence-linked · Open research infrastructure")

sources=D['sources']; claims=D['claims']; plants=D['plants']; microbes=D['microorganisms']; measures=D['measurements']

def source_label(sid):
    row=sources[sources.source_id==sid]
    if row.empty: return sid
    r=row.iloc[0]; return f"{sid} · {r.get('title','')} ({r.get('year','')})"

def source_url(sid):
    row=sources[sources.source_id==sid]
    return '' if row.empty else row.iloc[0].get('source_url','')

def hero(title,subtitle):
    st.markdown(f"""<div class="hadia-hero"><span class="tag">JHARKHAND</span><span class="tag">OPEN DATA</span><span class="tag">EVIDENCE-LINKED</span><h1>{title}</h1><p>{subtitle}</p></div>""",unsafe_allow_html=True)

def metric_row():
    cols=st.columns(5)
    vals=[("Sources",len(sources)),("Evidence claims",len(claims)),("Plants / lichens",len(plants)),("Microbial records",len(microbes)),("Measurements",len(measures))]
    for c,(k,v) in zip(cols,vals): c.metric(k,f"{v:,}")

if page=="Home":
    hero("HADIA","Jharkhand's living rice-beer heritage, organized as transparent, searchable and reusable evidence — without pretending that the internet contains all community knowledge.")
    metric_row()
    st.markdown("### One home for scattered knowledge")
    a,b,c=st.columns(3)
    with a: st.markdown('<div class="card"><h3>🌿 Tradition</h3><p>Explore Ranu, plants, preparation terminology, festivals and source-reported community contexts.</p></div>',unsafe_allow_html=True)
    with b: st.markdown('<div class="card"><h3>🔬 Science</h3><p>Inspect microbial, chemical, nutritional and fermentation measurements with their methods, geography and citations.</p></div>',unsafe_allow_html=True)
    with c: st.markdown('<div class="card"><h3>🔗 Evidence</h3><p>Every claim travels with a source. Regional differences and apparent contradictions are preserved instead of averaged away.</p></div>',unsafe_allow_html=True)
    st.markdown("### What this release can — and cannot — say")
    st.info("HADIA-KB maps **publicly documented and retrievable evidence**. It does not claim to contain all oral, household, community-held or unpublished knowledge about Handia/Hadia/Haria.")
    cat=claims['claim_category'].replace('', 'Unclassified').value_counts().reset_index(); cat.columns=['Category','Claims']
    fig=px.bar(cat,x='Claims',y='Category',orientation='h',title='Current evidence corpus by claim category')
    fig.update_layout(height=max(360,26*len(cat)+130),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',showlegend=False)
    st.plotly_chart(fig,use_container_width=True)

elif page=="Evidence Explorer":
    hero("Evidence Explorer","Search the claim-level dataset, filter it by geography, category or reported beverage name, and export exactly what you see.")
    q=st.text_input("Search all claim fields",placeholder="Try: Ranu, Sarhul, fermentation, Lactobacillus, Khunti …")
    c1,c2,c3=st.columns(3)
    with c1: scope=st.selectbox("Geographic scope",["All"]+sorted([x for x in claims.geographic_scope.unique() if x]))
    with c2: cat=st.selectbox("Category",["All"]+sorted([x for x in claims.claim_category.unique() if x]))
    with c3: nm=st.selectbox("Name as reported",["All"]+sorted([x for x in claims.name_as_reported.unique() if x]))
    f=filter_df(claims,q,geographic_scope=scope,claim_category=cat,name_as_reported=nm)
    st.metric("Matching claims",len(f)); st.dataframe(f,use_container_width=True,hide_index=True,height=440)
    d1,d2=st.columns(2)
    d1.download_button("⬇ Download filtered CSV",to_csv_bytes(f),"HADIA_filtered_claims.csv","text/csv",use_container_width=True)
    d2.download_button("⬇ Download filtered JSON",to_json_bytes(f),"HADIA_filtered_claims.json","application/json",use_container_width=True)

elif page=="Jharkhand Atlas":
    hero("Jharkhand Evidence Atlas","A map of where the current corpus explicitly places evidence. Display coordinates are approximate district/state visualization points, not research geocodes.")
    loc=D['locations'].copy()
    if not loc.empty:
        loc['display_lat']=pd.to_numeric(loc['display_lat'],errors='coerce'); loc['display_lon']=pd.to_numeric(loc['display_lon'],errors='coerce')
        # counts by scope text approximation
        loc['evidence_mentions']=loc.apply(lambda r: claims['geographic_scope'].str.contains(str(r.get('district') or r.get('state')),case=False,regex=False).sum(),axis=1)
        fig=px.scatter_map(loc.dropna(subset=['display_lat','display_lon']),lat='display_lat',lon='display_lon',size='evidence_mentions',hover_name='district',hover_data=['state','precision','evidence_mentions','coordinate_basis'],zoom=4.3,height=570)
        fig.update_layout(map_style='open-street-map',margin=dict(l=0,r=0,t=0,b=0))
        st.plotly_chart(fig,use_container_width=True)
    jh=claims[claims.geographic_scope.str.contains('Jharkhand',case=False,na=False)]
    st.markdown("### Explicitly Jharkhand-scoped evidence")
    st.dataframe(jh[['claim_id','claim_category','claim_text','geographic_scope','source_id']],use_container_width=True,hide_index=True)

elif page=="Ranu & Plants":
    hero("Ranu & Plant Atlas","See exactly which plant or lichen records were reported in accessible starter-culture evidence, with community and geographic context retained.")
    q=st.text_input("Search plant / starter records")
    f=filter_df(plants,q)
    st.dataframe(f,use_container_width=True,hide_index=True,height=430)
    if not f.empty:
        ctx_col='starter_or_context' if 'starter_or_context' in f.columns else ('starter' if 'starter' in f.columns else None)
        if ctx_col:
            vc=f[ctx_col].replace('', 'NR').value_counts().reset_index(); vc.columns=['Starter/context','Records']
            st.plotly_chart(px.bar(vc,x='Starter/context',y='Records',title='Starter-culture contexts represented'),use_container_width=True)
    st.download_button("⬇ Download plant atlas CSV",to_csv_bytes(f),"HADIA_plants.csv","text/csv")

elif page=="Microbes & Chemistry":
    hero("Microbes & Chemistry","Laboratory findings remain attached to their original beverage name, geography, method and source — preventing West Bengal or Odisha measurements from silently becoming Jharkhand facts.")
    tab1,tab2=st.tabs(["🦠 Microorganisms","🧪 Measurements"])
    with tab1:
        st.dataframe(microbes,use_container_width=True,hide_index=True)
        if not microbes.empty and 'identification_method' in microbes:
            vc=microbes.identification_method.value_counts().reset_index(); vc.columns=['Method','Records']
            st.plotly_chart(px.bar(vc,x='Records',y='Method',orientation='h',title='Identification methods'),use_container_width=True)
    with tab2:
        st.dataframe(measures,use_container_width=True,hide_index=True)
        st.warning("Numerical results are study-specific. Different sample states, dilution, methods, geography and fermentation stages may make values non-comparable.")

elif page=="Culture & Policy":
    hero("Culture & Policy","Handia's documentation includes ritual life and government policy — including evidence that can pull in different directions. HADIA preserves both.")
    cult=claims[claims.claim_category.isin(['culture','diet/culture'])]
    pol=claims[claims.claim_category.isin(['policy','law','regulation'])]
    c1,c2=st.columns(2)
    with c1:
        st.subheader("Culture")
        for _,r in cult.iterrows(): st.markdown(f"**{r.claim_id}** — {r.claim_text}\n\n*{r.geographic_scope} · {r.source_id}*")
    with c2:
        st.subheader("Policy & law")
        for _,r in pol.iterrows(): st.markdown(f"**{r.claim_id}** — {r.claim_text}\n\n*{r.geographic_scope} · {r.source_id}*")

elif page=="Evidence Passport":
    hero("Handia Evidence Passport","Open a claim as an auditable evidence object: statement, scope, terminology, caution and source travel together.")
    cid=st.selectbox("Claim",claims.claim_id.tolist(),format_func=lambda x: f"{x} — {claims.loc[claims.claim_id==x,'claim_text'].iloc[0][:85]}…")
    r=claims[claims.claim_id==cid].iloc[0]
    s=sources[sources.source_id==r.source_id].iloc[0]
    st.markdown(f"""<div class="passport"><h3>{r.claim_id}</h3><b>Reported finding</b><p>{r.claim_text}</p><b>Geographic scope</b><p>{r.geographic_scope}</p><b>Name as reported</b><p>{r.name_as_reported}</p><b>Evidence class</b><p>{r.claim_category} · {r.evidence_directness} · {r.source_quality}</p><b>Caution</b><p>{r.caution or 'No additional caution recorded.'}</p><b>Source</b><p>{s.title} ({s.year}) · {s.source_id}</p></div>""",unsafe_allow_html=True)
    if s.source_url: st.link_button("Open original source",s.source_url)
    st.download_button("Download this passport (JSON)",json.dumps({"claim":r.to_dict(),"source":s.to_dict()},ensure_ascii=False,indent=2).encode('utf-8'),f"{cid}_passport.json","application/json")

elif page=="Knowledge Graph":
    hero("HADIA Knowledge Graph","A source-carrying graph connects evidence claims to sources, reported names, scopes, categories, plants and microorganisms.")
    rel=D['relations']; max_edges=st.slider("Edges to visualize",40,min(250,len(rel)),min(120,len(rel)),10) if len(rel)>=40 else len(rel)
    rr=rel.head(max_edges)
    G=nx.Graph();
    for _,r in rr.iterrows(): G.add_edge(r.subject_id,r.object_id,predicate=r.predicate)
    pos=nx.spring_layout(G,seed=42,k=1/math.sqrt(max(1,G.number_of_nodes())))
    xe=[]; ye=[]
    for a,b in G.edges():
        x0,y0=pos[a];x1,y1=pos[b];xe += [x0,x1,None];ye += [y0,y1,None]
    edge=go.Scatter(x=xe,y=ye,mode='lines',line=dict(width=.7,color='#B89B72'),hoverinfo='none')
    xn=[];yn=[];text=[]
    for n in G.nodes(): x,y=pos[n];xn.append(x);yn.append(y);text.append(str(n))
    node=go.Scatter(x=xn,y=yn,mode='markers',text=text,hovertemplate='%{text}<extra></extra>',marker=dict(size=9,color='#C94F18',line=dict(width=1,color='#FFF9ED')))
    fig=go.Figure([edge,node]);fig.update_layout(height=650,showlegend=False,margin=dict(l=0,r=0,t=20,b=0),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis=dict(visible=False),yaxis=dict(visible=False))
    st.plotly_chart(fig,use_container_width=True)
    st.caption("Graph edges are generated from the frozen dataset and carry a source identifier in `relations.csv`.")

elif page=="Research Gaps":
    hero("Documented Knowledge Gaps","Red means 'poorly represented in this corpus', not 'absent in Jharkhand'. This distinction is central to HADIA's evidence ethics.")
    gaps=D['gaps'].copy(); gaps['current_jharkhand_claim_count']=pd.to_numeric(gaps.current_jharkhand_claim_count,errors='coerce').fillna(0)
    fig=px.bar(gaps,x='current_jharkhand_claim_count',y='topic_or_scope',orientation='h',title='Jharkhand-scoped claim coverage in HADIA-KB v1.0')
    st.plotly_chart(fig,use_container_width=True)
    st.dataframe(gaps,use_container_width=True,hide_index=True)
    st.markdown("### Preserved contextual differences")
    st.dataframe(D['contradictions'],use_container_width=True,hide_index=True)

elif page=="Sources":
    hero("Source Library","The bibliography behind the dataset. Search titles, venues, geography, source type and reported terminology; open the original source directly.")
    q=st.text_input("Search source library")
    f=filter_df(sources,q)
    st.dataframe(f,use_container_width=True,hide_index=True,height=500,column_config={"source_url":st.column_config.LinkColumn("Source URL")})
    st.download_button("⬇ Download source library CSV",to_csv_bytes(f),"HADIA_sources.csv","text/csv")

elif page=="Download Data":
    hero("Download HADIA-KB","Use the entire frozen release or export individual tables. Citation and provenance stay with the data.")
    metric_row()
    st.markdown("### Complete research release")
    st.download_button("⬇ HADIA-KB v1.0 — all tables (ZIP)",tables_zip_bytes({k:v for k,v in D.items() if not v.empty}),"HADIA_KB_v1_0_CSV.zip","application/zip",use_container_width=True)
    xlsx_path=Path('data/releases/v1.0/HADIA_KB_v1_0.xlsx')
    if xlsx_path.exists(): st.download_button("⬇ HADIA-KB v1.0 — Excel workbook",xlsx_path.read_bytes(),"HADIA_KB_v1_0.xlsx","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",use_container_width=True)
    st.markdown("### Individual tables")
    cols=st.columns(3)
    for i,(name,df) in enumerate(D.items()):
        if df.empty: continue
        with cols[i%3]: st.download_button(f"CSV · {name}",to_csv_bytes(df),f"HADIA_{name}.csv","text/csv",key=f"d_{name}",use_container_width=True)
    st.info("Download the complete archived HADIA-KB v1.0.0 release from Zenodo: https://doi.org/10.5281/zenodo.22132285")

else:
    hero("About HADIA","A digital heritage and scientific evidence infrastructure designed to make documented knowledge about Handia easier to discover, audit and reuse.")
    st.markdown("### Research boundary")
    st.write(META['scope'])
    for x in META['limitations']: st.markdown(f"- {x}")
    st.markdown("### Data integrity")
    errors=validate_all(D)
    if errors: st.error("Validation issues detected: " + "; ".join(errors))
    else: st.success("All packaged relational integrity checks passed for this release.")
    st.markdown("### Licensing")
    st.markdown("**Software:** Apache License 2.0  \n**Dataset compilation/annotations/schema/docs:** CC BY 4.0  \n**Third-party publications and linked source material:** retain their own rights.")
st.markdown("### Citation")
st.markdown(
    "**Paper:** Akhtar, M. A. K. (2026). *HADIA-KB: Evidence-Preserving Digital Knowledge Infrastructure for Jharkhand's Traditional Rice Beer* [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.22132847"
)

st.markdown(
    "**Software:** Akhtar, M. A. K. (2026). *HADIA-KB: An Evidence-Linked Knowledge Base and Interactive Research Platform for Handia/Hadia/Haria* (Version V1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.22132285"
)

st.markdown('<div class="foot">HADIA · Evidence before assertion · Copyright (C) 2026 Mohammad Amir Khusru Akhtar</div>',unsafe_allow_html=True)
