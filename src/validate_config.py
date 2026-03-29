#!/usr/bin/env python3
"""
Agent Protocol Stack - 配置验证脚本
验证用户配置并生成注册表
"""

import json
import os
import sys
from datetime import datetime

class ConfigValidator:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None
        self.errors = []
        self.warnings = []
        self.agent_ids = []
        self.spines = []
        
    def load_config(self):
        """加载配置文件"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.config = self._parse_yaml(content)
            print(f"✅ 配置加载成功: {self.config_path}")
            return True
        except FileNotFoundError:
            self.errors.append(f"配置文件不存在: {self.config_path}")
            return False
        except Exception as e:
            self.errors.append(f"解析错误: {e}")
            return False
    
    def _parse_yaml(self, content):
        """简单YAML解析器"""
        result = {}
        lines = content.split('\n')
        current_list = []
        in_list = False
        list_key = None
        
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            
            indent = len(line) - len(line.lstrip())
            
            # 检测列表
            if stripped.startswith('-'):
                in_list = True
                list_key = None
                content = stripped[1:].strip()
                if ':' in content:
                    key = content.split(':')[0].strip()
                    value = content.split(':', 1)[1].strip() if len(content.split(':')) > 1 else None
                    current_list.append({key: value} if value else key)
                    list_key = None
                else:
                    current_list.append(content)
            elif ':' in stripped and not in_list:
                key = stripped.split(':')[0].strip()
                value = stripped.split(':', 1)[1].strip()
                if value:
                    result[key] = value
                else:
                    result[key] = {}
                    list_key = key
                    in_list = False
            elif in_list and ':' in stripped:
                current_list.append({})
                
        if current_list:
            result['agents'] = current_list
            
        return result
    
    def validate_agents(self):
        """验证Agent定义"""
        print("\n" + "="*60)
        print("📋 验证 Agent 定义")
        print("="*60)
        
        if 'agents' not in self.config:
            self.errors.append("缺少 agents 配置")
            return False
            
        agents = self.config['agents']
        if not agents:
            self.errors.append("agents 列表为空")
            return False
            
        print(f"   Agent总数: {len(agents)}")
        
        for agent in agents:
            if isinstance(agent, dict):
                agent_id = agent.get('id', agent[0] if isinstance(agent, list) and agent else '')
                role = agent.get('role', '')
                
                if isinstance(agent, list) and agent:
                    for item in agent:
                        if isinstance(item, dict):
                            agent_id = item.get('id', list(item.keys())[0])
                            role = item.get('role', '')
                            break
                
                self.agent_ids.append(agent_id)
                
                if role == 'spine':
                    self.spines.append(agent_id)
                    print(f"   ✅ Spine节点: {agent_id}")
                elif role:
                    print(f"   ✅ Leaf节点: {agent_id}")
                    
        if len(self.spines) == 0:
            self.errors.append("必须至少有一个Spine节点")
        elif len(self.spines) > 1:
            self.errors.append(f"Spine节点只能有1个，当前有 {len(self.spines)} 个")
        else:
            print(f"   ✅ Spine验证通过")
            
        return len(self.errors) == 0
        
    def validate_routing(self):
        """验证路由配置"""
        print("\n" + "="*60)
        print("🎯 验证 路由配置")
        print("="*60)
        
        if 'routing' not in self.config:
            self.warnings.append("缺少 routing 配置")
            return True
            
        routing = self.config['routing']
        if 'rules' in routing:
            print(f"   路由规则数: {len(routing['rules'])}")
            
        return True
        
    def generate_registry(self):
        """生成注册表"""
        print("\n" + "="*60)
        print("📊 生成 Agent 注册表")
        print("="*60)
        
        registry = {
            "version": "1.0",
            "generated_at": datetime.now().isoformat(),
            "cluster_name": self.config.get('cluster', {}).get('name', 'unknown'),
            "agents": []
        }
        
        for agent in self.config.get('agents', []):
            if isinstance(agent, dict):
                registry['agents'].append({
                    "id": agent.get('id', ''),
                    "name": agent.get('name', ''),
                    "role": agent.get('role', ''),
                    "type": agent.get('type', ''),
                    "capabilities": agent.get('capabilities', []),
                    "status": "active"
                })
            elif isinstance(agent, list):
                for item in agent:
                    if isinstance(item, dict):
                        registry['agents'].append({
                            "id": item.get('id', ''),
                            "name": item.get('name', ''),
                            "role": item.get('role', ''),
                            "type": item.get('type', ''),
                            "capabilities": item.get('capabilities', []),
                            "status": "active"
                        })
                        
        output_path = os.path.join(os.path.dirname(self.config_path), '../registry/AgentRegistry.json')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)
            
        print(f"   ✅ 注册表已生成: {output_path}")
        return registry
        
    def run_validation(self):
        """运行验证"""
        print("\n" + "="*60)
        print("🚀 Agent Protocol Stack - 配置验证")
        print("="*60)
        
        if not self.load_config():
            return False
            
        if not self.validate_agents():
            return False
            
        self.validate_routing()
        
        if len(self.errors) == 0:
            self.generate_registry()
        
        print("\n" + "="*60)
        print("📋 验证结果")
        print("="*60)
        
        if not self.errors:
            print("\n✅ 验证通过!")
        else:
            print("\n❌ 验证失败:")
            for e in self.errors:
                print(f"   - {e}")
                
        if self.warnings:
            print("\n⚠️ 警告:")
            for w in self.warnings:
                print(f"   - {w}")
                
        return len(self.errors) == 0

def main():
    import argparse
    parser = argparse.ArgumentParser(description='验证APS配置')
    parser.add_argument('--config', default='config/UserConfig.yaml', help='配置文件路径')
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(os.path.dirname(base_dir), args.config)
    
    if not os.path.exists(config_path):
        config_path = args.config
        
    validator = ConfigValidator(config_path)
    success = validator.run_validation()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()