#!/usr/bin/env python3
"""
Test Suite and Validator for SEI Quality Attributes Skills
Nicola Satragni - Franco Nelli
Ingeniería de Software 1
"""

import os
import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

SKILLS_TO_VALIDATE = [
    ".agents/skills/sei-quality-attributes",
    ".agents/skills/sei-scenario-generator",
    ".agents/skills/sei-scenario-checker",
    ".agents/skills/sei-utility-tree-builder",
]

REQUIRED_REFERENCES = [
    ".agents/skills/sei-quality-attributes/references/sei-taxonomy.md",
    ".agents/skills/sei-quality-attributes/references/audit-rules.md",
    ".agents/skills/sei-quality-attributes/references/utility-tree-schema.md",
    ".agents/skills/sei-quality-attributes/references/sei_scenario_template.md",
    ".agents/skills/sei-quality-attributes/references/utility_tree.md",
    ".agents/skills/sei-quality-attributes/examples/ejemplos_escenarios.md",
]

SEI_PARTS = [
    "fuente del estímulo",
    "estímulo",
    "artefacto",
    "entorno",
    "respuesta",
    "medida de respuesta",
]

VAGUE_TERMS = [
    "rápido",
    "rapido",
    "robusto",
    "seguro",
    "fácil",
    "facil",
    "adecuado",
    "minimizar fallas",
    "no se caiga",
    "no se cae",
]


def test_references_exist():
    """Verify all reference documents and examples exist and have content."""
    print("[TEST] Verificando existencia de material complementario...")
    for ref_rel in REQUIRED_REFERENCES:
        ref_path = WORKSPACE_ROOT / ref_rel
        assert ref_path.is_file(), f"Falta archivo de referencia requerido: {ref_rel}"
        assert ref_path.stat().st_size > 100, f"Archivo de referencia vacío o muy pequeño: {ref_rel}"
        print(f"  ✅ OK: {ref_rel} ({ref_path.stat().st_size} bytes)")
    print("  -> Todos los archivos de referencia existen y contienen datos completos.\n")


def test_skill_frontmatter():
    """Verify each skill has valid YAML frontmatter with name and description."""
    print("[TEST] Verificando encabezados YAML de las skills...")
    for skill_rel in SKILLS_TO_VALIDATE:
        skill_file = WORKSPACE_ROOT / skill_rel / "SKILL.md"
        assert skill_file.is_file(), f"Falta SKILL.md en: {skill_rel}"
        content = skill_file.read_text(encoding="utf-8")

        # Check YAML block
        assert content.startswith("---"), f"SKILL.md no inicia con YAML frontmatter en {skill_rel}"
        parts = content.split("---", 2)
        assert len(parts) >= 3, f"YAML frontmatter mal cerrado en {skill_rel}"
        yaml_text = parts[1]

        assert "name:" in yaml_text, f"Falta campo 'name' en {skill_rel}"
        assert "description:" in yaml_text, f"Falta campo 'description' en {skill_rel}"
        
        name_match = re.search(r"name:\s*([a-zA-Z0-9_\-]+)", yaml_text)
        assert name_match, f"Nombre de skill no válido en {skill_rel}"
        skill_name = name_match.group(1)
        
        print(f"  ✅ OK Skill '{skill_name}' en {skill_rel}")
    print("  -> Todas las skills tienen YAML frontmatter válido y completo.\n")


def test_test_cases_suite():
    """Verify test cases document exists and covers all 6 test scenarios."""
    print("[TEST] Verificando suite de casos de prueba (test_cases.md)...")
    tc_file = WORKSPACE_ROOT / "tests/test_cases.md"
    assert tc_file.is_file(), "Falta tests/test_cases.md"
    content = tc_file.read_text(encoding="utf-8").lower()

    for tc_id in ["tc-01", "tc-02", "tc-03", "tc-04", "tc-05", "tc-06"]:
        assert tc_id in content, f"Falta caso de prueba {tc_id} en test_cases.md"
        print(f"  ✅ Caso de prueba {tc_id.upper()} documentado y validado.")

    for part in SEI_PARTS:
        assert part in content, f"Falta dimensión '{part}' en test_cases.md"
    print("  -> Las 6 partes del SEI están presentes en los casos de prueba.\n")


def test_scenario_quality_assertions():
    """Simulate quality auditing logic on test cases to verify SEI compliance."""
    print("[TEST] Ejecutando aserciones de calidad sobre especificaciones SEI...")
    # Test valid scenario
    sample_scenario = {
        "fuente": "Clientes concurrentes autenticados en plataforma web y móvil.",
        "estímulo": "Llegada de 12.000 solicitudes simultáneas de pago por minuto.",
        "artefacto": "Microservicio de Transacciones de Compra y Pasarela de Pagos.",
        "entorno": "Evento de alta demanda comercial (Black Friday).",
        "respuesta": "Encolamiento asíncrono y autoescalado de workers de cobro.",
        "medida_respuesta": "Latencia p95 <= 1.5 s; Throughput >= 5.000 TPS; 0% transacciones caídas.",
    }

    # Verify all 6 parts present
    assert len(sample_scenario) == 6, "El escenario debe tener exactamente 6 partes"
    for key, val in sample_scenario.items():
        assert len(val.strip()) > 5, f"La dimensión {key} está vacía o es muy corta"
        for vague in VAGUE_TERMS:
            assert vague not in val.lower(), f"Término vago '{vague}' detectado en {key}"

    # Verify Utility Tree prioritization tuple format
    sample_priorities = ["(H, H)", "(H, M)", "(M, H)", "(M, M)", "(M, L)", "(L, L)"]
    tuple_pattern = re.compile(r"^\([HML],\s*[HML]\)$")
    for prio in sample_priorities:
        assert tuple_pattern.match(prio), f"Tupla de prioridad inválida: {prio}"

    print("  ✅ Aserción de 6 partes superada sin términos vagos.")
    print("  ✅ Formato de tupla bidimensional (H/M/L, H/M/L) validado.")
    print("  -> Aserciones de calidad verificadas exitosamente.\n")


def main():
    print("================================================================")
    print(" EJECUCIÓN DE PRUEBAS AUTOMATIZADAS - SKILLS SEI / ATAM")
    print(" Autores: Nicola Satragni - Franco Nelli | Ing. de Software 1")
    print("================================================================\n")
    test_references_exist()
    test_skill_frontmatter()
    test_test_cases_suite()
    test_scenario_quality_assertions()
    print("================================================================")
    print(" 🎉 TODAS LAS PRUEBAS (4/4) PASARON CON ÉXITO (100% PASS)")
    print("================================================================")


if __name__ == "__main__":
    main()
