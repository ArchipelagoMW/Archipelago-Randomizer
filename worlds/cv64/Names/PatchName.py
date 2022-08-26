stage_select_overwrite = [
    0x8F, 0xA6, 0x00, 0x18,  # LW	 A2, 0x0018 (SP)
    0xA0, 0x60, 0x64, 0x37,  # SB	 R0, 0x6437 (V1)
    0x10, 0x00, 0x00, 0x29,  # B	 0x8012ACE8
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x3C, 0x0A, 0x80, 0x39,  # LUI	 T2, 0x8039
    0x25, 0x4A, 0x9C, 0x4B,  # ADDIU T2, T2, 0x9C4B
    0x81, 0x4B, 0x00, 0x00,  # LB	 T3, 0x0000 (T2)
    0x81, 0x4C, 0x00, 0x01,  # LB	 T4, 0x0001 (T2)
    0x01, 0x8C, 0x60, 0x21,  # ADDU	 T4, T4, T4
    0x01, 0x6C, 0x68, 0x21,  # ADDU	 T5, T3, T4
    0x24, 0x0C, 0x00, 0x0A,  # ADDIU T4, R0, 0x000A
    0x01, 0xAC, 0x00, 0x1B,  # DIVU	 T5, T4
    0x00, 0x00, 0x30, 0x12,  # MFLO	 A2
    0x24, 0xC6, 0x00, 0x01,  # ADDIU A2, A2, 0x0001
    0x28, 0xCA, 0x00, 0x09,  # SLTI	 T2, A2, 0x0009
    0x51, 0x40, 0x00, 0x01,  # BEQZL T2, 0x8012AC7C
    0x24, 0x06, 0x00, 0x08,  # ADDIU A2, R0, 0x0008
    0x03, 0x20, 0x00, 0x08,  # JR	 T9
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x00, 0x00, 0x00, 0x00   # NOP
]

remote_item_and_warp = [
    # Stage Select menu checks
    0x3C, 0x08, 0x80, 0x39,  # LUI   T0, 0x8039
    0x91, 0x09, 0x9E, 0xFB,  # LBU   T1, 0x9EFB (T0)
    0x91, 0x0A, 0x9E, 0xFF,  # LBU   T2, 0x9EFF (T0)
    0x01, 0x2A, 0x48, 0x21,  # ADDU  T1, T1, T2
    0x91, 0x0A, 0x9C, 0xCF,  # LBU   T2, 0x9CCF (T0)
    0x01, 0x2A, 0x48, 0x21,  # ADDU	 T1, T1, T2
    0x91, 0x0A, 0x9E, 0xEF,  # LBU	 T2, 0x9EEF (T0)
    0x01, 0x2A, 0x48, 0x21,  # ADDU	 T1, T1, T2
    0x91, 0x0A, 0x9C, 0xD3,  # LBU	 T2, 0x9CD3 (T0)
    0x01, 0x2A, 0x48, 0x21,  # ADDU	 T1, T1, T2
    0x3C, 0x08, 0x80, 0x38,  # LUI	 T0, 0x8038
    0x91, 0x0A, 0x7A, 0xDD,  # LBU	 T2, 0x7ADD (T0)
    0x01, 0x2A, 0x48, 0x21,  # ADDU	 T1, T1, T2
    0x15, 0x20, 0x00, 0x16,  # BNEZ	 T1, 0x801836BC
    0x3C, 0x08, 0x80, 0x34,  # LUI	 T0, 0x8034
    0x91, 0x09, 0x27, 0xA9,  # LBU	 T1, 0x27A9 (T0)
    0x24, 0x0A, 0x00, 0x01,  # ADDIU T2, R0, 0x0001
    0x15, 0x2A, 0x00, 0x14,  # BNE	 T1, T2, 0x801836C4
    0x3C, 0x08, 0x80, 0x0D,  # LUI	 T0, 0x800D
    0x85, 0x09, 0x5E, 0x20,  # LH	 T1, 0x5E20 (T0)
    0x24, 0x08, 0x20, 0x20,  # ADDIU T0, R0, 0x2020
    0x15, 0x09, 0x00, 0x10,  # BNE	 T0, T1, 0x801836C4
    0x3C, 0x08, 0x80, 0x35,  # LUI	 T0, 0x8035
    0x91, 0x08, 0xF7, 0xD8,  # LBU	 T0, 0xF7D8 (T0)
    0x24, 0x09, 0x00, 0x20,  # ADDIU T1, R0, 0x0020
    0x11, 0x09, 0x00, 0x0C,  # BEQ	 T0, T1, 0x801836C4
    0x3C, 0x08, 0x80, 0x39,  # LUI	 T0, 0x8039
    0x91, 0x09, 0x9C, 0x88,  # LBU	 T1, 0x9C88 (T0)
    0x31, 0x29, 0x00, 0x80,  # ANDI	 T1, T1, 0x0080
    0x91, 0x0A, 0x9B, 0xFA,  # LBU	 T1, 0x9BFA (T0)
    0x31, 0x4A, 0x00, 0x01,  # ANDI	 T1, T1, 0x0001
    0x01, 0x2A, 0x48, 0x21,  # ADDU	 T1, T1, T2
    0x15, 0x20, 0x00, 0x05,  # BNEZ	 T1, 0x801836C4
    0x24, 0x08, 0xFF, 0xFC,  # ADDIU T0, R0, 0xFFFC
    0x3C, 0x09, 0x80, 0x34,  # LUI	 T1, 0x8034
    0xAD, 0x28, 0x20, 0x84,  # SW	 T0, 0x2084 (T1)
    0x03, 0xE0, 0x00, 0x08,  # JR	 RA
    # Item-rewarding byte checks
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x3C, 0x0B, 0x80, 0x39,  # LUI	 T3, 0x8039
    0x91, 0x69, 0x9B, 0xE0,  # LBU	 T1, 0x9BE0 (T3)
    0x11, 0x20, 0x00, 0x05,  # BEQZ	 T1, 0x801836E4
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x25, 0x29, 0xFF, 0xFF,  # ADDIU T1, T1, 0xFFFF
    0xA1, 0x69, 0x9B, 0xE0,  # SB	 T1, 0x9BE0 (T3)
    0x03, 0xE0, 0x00, 0x08,  # JR    RA
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x3C, 0x08, 0x80, 0x34,  # LUI 	 T0, 0x8034
    0x91, 0x08, 0x28, 0x91,  # LBU	 T0, 0x2891 (T0)
    0x24, 0x09, 0x00, 0x02,  # ADDIU T1, R0, 0x0002
    0x15, 0x09, 0x00, 0x05,  # BNE	 T0, T1, 0x80183708
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x25, 0x6B, 0x9B, 0xDF,  # ADDIU T3, T3, 0x9BDF
    0x91, 0x64, 0x00, 0x00,  # LBU	 A0, 0x0000 (T3)
    0x14, 0x80, 0x00, 0x03,  # BNEZ	 A0, 0x80183710
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x03, 0xE0, 0x00, 0x08,  # JR    RA
    0x00, 0x00, 0x00, 0x00,  # NOP
    0x24, 0x09, 0x00, 0x0F,  # ADDIU T1, R0, 0x000F
    0xA1, 0x69, 0x00, 0x01,  # SB	 T1, 0x0001 (T3)
    0x08, 0x04, 0xED, 0xCE,  # J	 0x8013B738
    0xA1, 0x60, 0x00, 0x00,  # SB	 R0, 0x0000 (T3)
]