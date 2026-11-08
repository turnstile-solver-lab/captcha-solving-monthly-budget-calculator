#!/usr/bin/env python3
"""
CapSolver AI Captcha Solving TCO Cost & Speed Calculator
Models monthly expenditure across reCAPTCHA v2/v3, Turnstile, FunCaptcha, and GeeTest.
"""

import sys

def calculate_capsolver_tco(monthly_captchas: int, captcha_type: str = "recaptcha_v2"):
    rates_per_1000 = {
        "turnstile": 0.60,
        "recaptcha_v2": 0.80,
        "recaptcha_v3": 1.00,
        "geetest": 0.80,
        "funcaptcha": 1.20,
        "aws_waf": 1.50
    }
    
    rate = rates_per_1000.get(captcha_type, 0.80)
    capsolver_cost = (monthly_captchas / 1000.0) * rate
    twocaptcha_cost = (monthly_captchas / 1000.0) * 2.20
    anticaptcha_cost = (monthly_captchas / 1000.0) * 1.80
    
    return {
        "monthly_captchas": monthly_captchas,
        "captcha_type": captcha_type,
        "unit_rate_per_1k": rate,
        "capsolver_cost_usd": round(capsolver_cost, 2),
        "twocaptcha_cost_usd": round(twocaptcha_cost, 2),
        "anticaptcha_cost_usd": round(anticaptcha_cost, 2),
        "savings_vs_twocaptcha": round(twocaptcha_cost - capsolver_cost, 2),
        "savings_vs_anticaptcha": round(anticaptcha_cost - capsolver_cost, 2)
    }

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    ctype = sys.argv[2] if len(sys.argv) > 2 else "recaptcha_v2"
    res = calculate_capsolver_tco(count, ctype)
    print(f"=== CapSolver TCO Calculation for {res['monthly_captchas']:,} {res['captcha_type']} ===")
    print(f"CapSolver Rate: ${res['unit_rate_per_1k']}/1,000")
    print(f"CapSolver Total: ${res['capsolver_cost_usd']}")
    print(f"2Captcha Equivalent: ${res['twocaptcha_cost_usd']} (Save ${res['savings_vs_twocaptcha']})")
    print(f"Anti-Captcha Equivalent: ${res['anticaptcha_cost_usd']} (Save ${res['savings_vs_anticaptcha']})")
