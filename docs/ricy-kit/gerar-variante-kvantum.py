from pathlib import Path
import xml.etree.ElementTree as E,configparser,shutil
b=Path('outputs/kde-outlines/KDE-Noctalia');b.mkdir(parents=True,exist_ok=True)
src=Path('work/catppuccin-kvantum/themes/catppuccin-mocha-mauve')
config=configparser.ConfigParser(interpolation=None,strict=False);config.optionxform=str;config.read(src/'catppuccin-mocha-mauve.kvconfig')
config['%General']['comment']='KDE-Noctalia: Catppuccin Mocha Mauve com contornos suaves'
config['%General']['reduce_window_opacity']='0'
config['%General']['shadowless_popup']='true'
config['%General']['menu_shadow_depth']='0'
config['%General']['popup_blurring']='false'
config['%General']['spread_menuitems']='false'
config['Menu']['frame.patternsize']='0'
config['Menu']['frame.expansion']='0'
config['%General']['reduce_menu_opacity']='0'
config['GeneralColors']['highlight.color']='#977dba'
config['GeneralColors']['highlight.text.color']='#000000'
for k in ['frame.top','frame.bottom','frame.left','frame.right']:config['Menu'][k]='12'
config['MenuItem']['frame.top']='4';config['MenuItem']['frame.bottom']='4'
for k in ['text.margin.top','text.margin.bottom']:config['MenuItem'][k]='0'
for k in ['frame.left','frame.right']:config['MenuItem'][k]='6'
for k in ['text.margin.left','text.margin.right']:config['MenuItem'][k]='2'
config['MenuItem']['min_height']='24'
config['%General']['menu_separator_height']='5'
config['MenuItem']['text.focus.color']='#000000';config['MenuItem']['text.press.color']='#000000'
with (b/'KDE-Noctalia.kvconfig').open('w') as f:config.write(f,space_around_delimiters=False)
ns='http://www.w3.org/2000/svg';E.register_namespace('',ns);E.register_namespace('xlink','http://www.w3.org/1999/xlink')
r=E.parse(src/'catppuccin-mocha-mauve.svg').getroot()
for parent in r.iter():
 for x in list(parent):
  i=x.get('id','')
  if i in {p+s for p in ['menu-normal','menuitem-normal'] for s in ['','-top','-bottom','-left','-right','-topleft','-topright','-bottomleft','-bottomright']}:parent.remove(x)
def elem(tag,parent,**attrs):return E.SubElement(parent,'{'+ns+'}'+tag,{k:str(v) for k,v in attrs.items()})
def frame(prefix,radius,fill,border=None):
 R=radius
 for i,part in enumerate(['','-top','-bottom','-left','-right','-topleft','-topright','-bottomleft','-bottomright']):
  g=elem('g',r,id=prefix+part,transform=f'translate({1000+i*50} 800)')
  if not part:elem('rect',g,x=0,y=0,width=16,height=16,fill=fill)
  elif part in ['-top','-bottom','-left','-right']:
   horizontal=part in ['-top','-bottom'];w,h=(16,R) if horizontal else (R,16)
   elem('rect',g,x=0,y=0,width=w,height=h,fill=fill)
   if border:
    coords={'-top':(0,.5,w,.5),'-bottom':(0,h-.5,w,h-.5),'-left':(.5,0,.5,h),'-right':(w-.5,0,w-.5,h)}[part]
    elem('rect',g,x=0 if horizontal else (0 if part=='-left' else w-1),y=(0 if part=='-top' else h-1) if horizontal else 0,width=w if horizontal else 1,height=1 if horizontal else h,fill=border)
  else:
   rotation={'-topleft':0,'-topright':90,'-bottomright':180,'-bottomleft':270}[part]
   q=elem('g',g,transform=f'rotate({rotation} {R/2} {R/2})')
   elem('path',q,d=f'M{R} 0 A{R} {R} 0 0 0 0 {R} L{R} {R} Z',fill=border or fill)
   if border:elem('path',q,d=f'M{R} 1 A{R-1} {R-1} 0 0 0 1 {R} L{R} {R} Z',fill=fill)
frame('menu-normal',12,'#313244','#46485c')
frame('menuitem-normal',6,'#977dba')
E.ElementTree(r).write(b/'KDE-Noctalia.svg',encoding='utf-8',xml_declaration=True)
shutil.copy2('work/catppuccin-kvantum/LICENSE',b/'LICENSE')
# Preserve any Kvantum config that existed before applying this variant.
p=Path.home()/'.config/Kvantum/kvantum.kvconfig'
backup=Path('outputs/kde-outlines/kvantum-config-antes')
if not backup.exists() and not Path('outputs/kde-outlines/kvantum-ausente-antes').exists():
 if p.exists():shutil.copy2(p,backup)
 else:Path('outputs/kde-outlines/kvantum-ausente-antes').touch()
install=Path.home()/'.config/Kvantum/KDE-Noctalia';install.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(b,install,dirs_exist_ok=True)
