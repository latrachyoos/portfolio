<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form esegue l'override del metodo Dispose per pulire l'elenco dei componenti.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Richiesto da Progettazione Windows Form
    Private components As System.ComponentModel.IContainer

    'NOTA: la procedura che segue è richiesta da Progettazione Windows Form
    'Può essere modificata in Progettazione Windows Form.  
    'Non modificarla nell'editor del codice.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.dgv = New System.Windows.Forms.DataGridView()
        Me.conto = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.dare = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.avere = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.radAcq = New System.Windows.Forms.RadioButton()
        Me.radVen = New System.Windows.Forms.RadioButton()
        Me.txtVal = New System.Windows.Forms.TextBox()
        Me.btnEconomia = New System.Windows.Forms.Button()
        Me.cmbScrit = New System.Windows.Forms.ComboBox()
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'dgv
        '
        Me.dgv.AllowUserToAddRows = False
        Me.dgv.AllowUserToDeleteRows = False
        Me.dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.dgv.Columns.AddRange(New System.Windows.Forms.DataGridViewColumn() {Me.conto, Me.dare, Me.avere})
        Me.dgv.Location = New System.Drawing.Point(363, 71)
        Me.dgv.Name = "dgv"
        Me.dgv.ReadOnly = True
        Me.dgv.RowTemplate.Height = 28
        Me.dgv.Size = New System.Drawing.Size(556, 342)
        Me.dgv.TabIndex = 0
        '
        'conto
        '
        Me.conto.HeaderText = "Conto"
        Me.conto.Name = "conto"
        Me.conto.ReadOnly = True
        Me.conto.Width = 125
        '
        'dare
        '
        Me.dare.HeaderText = "Dare"
        Me.dare.Name = "dare"
        Me.dare.ReadOnly = True
        '
        'avere
        '
        Me.avere.HeaderText = "Avere"
        Me.avere.Name = "avere"
        Me.avere.ReadOnly = True
        '
        'radAcq
        '
        Me.radAcq.AutoSize = True
        Me.radAcq.Checked = True
        Me.radAcq.Location = New System.Drawing.Point(34, 71)
        Me.radAcq.Name = "radAcq"
        Me.radAcq.Size = New System.Drawing.Size(110, 24)
        Me.radAcq.TabIndex = 1
        Me.radAcq.TabStop = True
        Me.radAcq.Text = "Acquistare"
        Me.radAcq.UseVisualStyleBackColor = True
        '
        'radVen
        '
        Me.radVen.AutoSize = True
        Me.radVen.Location = New System.Drawing.Point(34, 101)
        Me.radVen.Name = "radVen"
        Me.radVen.Size = New System.Drawing.Size(95, 24)
        Me.radVen.TabIndex = 2
        Me.radVen.Text = "Vendere"
        Me.radVen.UseVisualStyleBackColor = True
        '
        'txtVal
        '
        Me.txtVal.Location = New System.Drawing.Point(34, 175)
        Me.txtVal.Name = "txtVal"
        Me.txtVal.Size = New System.Drawing.Size(212, 26)
        Me.txtVal.TabIndex = 3
        Me.txtVal.Text = "12345"
        '
        'btnEconomia
        '
        Me.btnEconomia.Location = New System.Drawing.Point(34, 224)
        Me.btnEconomia.Name = "btnEconomia"
        Me.btnEconomia.Size = New System.Drawing.Size(211, 63)
        Me.btnEconomia.TabIndex = 4
        Me.btnEconomia.Text = "Button1"
        Me.btnEconomia.UseVisualStyleBackColor = True
        '
        'cmbScrit
        '
        Me.cmbScrit.DropDownWidth = 125
        Me.cmbScrit.FormattingEnabled = True
        Me.cmbScrit.Location = New System.Drawing.Point(252, 173)
        Me.cmbScrit.Name = "cmbScrit"
        Me.cmbScrit.Size = New System.Drawing.Size(88, 28)
        Me.cmbScrit.TabIndex = 5
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(9.0!, 20.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1011, 585)
        Me.Controls.Add(Me.cmbScrit)
        Me.Controls.Add(Me.btnEconomia)
        Me.Controls.Add(Me.txtVal)
        Me.Controls.Add(Me.radVen)
        Me.Controls.Add(Me.radAcq)
        Me.Controls.Add(Me.dgv)
        Me.Name = "Form1"
        Me.Text = "Form1"
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents dgv As System.Windows.Forms.DataGridView
    Friend WithEvents radAcq As System.Windows.Forms.RadioButton
    Friend WithEvents radVen As System.Windows.Forms.RadioButton
    Friend WithEvents txtVal As System.Windows.Forms.TextBox
    Friend WithEvents btnEconomia As System.Windows.Forms.Button
    Friend WithEvents cmbScrit As System.Windows.Forms.ComboBox
    Friend WithEvents conto As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents dare As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents avere As System.Windows.Forms.DataGridViewTextBoxColumn

End Class
