#!/usr/bin/env python3
"""Compile tests against the actual header and AnimationManager/MotionService from the source."""
import argparse,os,subprocess,tempfile
from pathlib import Path

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--fonte',type=Path,default=Path(os.environ.get('XDG_CACHE_HOME',Path.home()/'.cache'))/'ricy-noctalia-src-5.2.1')
 args=parser.parse_args();root=args.fonte/'src'
 with tempfile.TemporaryDirectory(prefix='ricy-icon-motion-test-') as temp:
  binary=Path(temp)/'validate-motion'
  subprocess.run(['c++','-std=c++23','-O1','-Wall','-Wextra','-I'+str(root),str(Path(__file__).with_suffix('.cpp')),str(root/'render/animation/animation_manager.cpp'),str(root/'render/animation/animation.cpp'),str(root/'render/animation/motion_service.cpp'),'-o',str(binary)],check=True)
  subprocess.run([str(binary)],check=True)
if __name__=='__main__':main()
